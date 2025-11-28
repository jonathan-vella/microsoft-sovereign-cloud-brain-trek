#!/usr/bin/env python3
"""
Encryption Key Hierarchy Diagram
L200-51: Key management hierarchy for sovereign cloud
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.security import KeyVaults
from diagrams.azure.storage import BlobStorage
from diagrams.azure.database import SQLDatabases
from diagrams.azure.compute import VM
from diagrams.onprem.security import Vault
from diagrams.generic.storage import Storage
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
os.makedirs(output_dir, exist_ok=True)

graph_attr = {
    "fontsize": "11",
    "bgcolor": "white",
    "pad": "0.4",
    "splines": "ortho",
    "nodesep": "0.6",
    "ranksep": "1.0"
}

with Diagram(
    "Encryption Key Hierarchy for Sovereign Cloud",
    filename=f"{output_dir}/encryption-key-hierarchy",
    show=False,
    direction="TB",
    graph_attr=graph_attr,
    outformat="svg"
):

    # Root of Trust
    with Cluster("Root of Trust (HSM)", graph_attr={"bgcolor": "#FFE6E6", "style": "rounded,bold"}):
        hsm = Vault("Hardware\nSecurity Module\n(FIPS 140-2 L3)")
        root_key = KeyVaults("Master Key\n(Never Leaves HSM)")

    # Key Encryption Keys
    with Cluster("Key Encryption Keys (KEKs)", graph_attr={"bgcolor": "#FFF4E6", "style": "rounded"}):
        kek_storage = KeyVaults("Storage KEK")
        kek_db = KeyVaults("Database KEK")
        kek_compute = KeyVaults("Compute KEK")
        kek_backup = KeyVaults("Backup KEK")

    # Data Encryption Keys
    with Cluster("Data Encryption Keys (DEKs)", graph_attr={"bgcolor": "#E8F4FD", "style": "rounded"}):
        with Cluster("Storage DEKs"):
            dek_blob = Storage("Blob DEK")
            dek_file = Storage("File DEK")
            dek_disk = Storage("Disk DEK")

        with Cluster("Database DEKs"):
            dek_sql = Storage("SQL TDE Key")
            dek_cosmos = Storage("Cosmos DEK")

        with Cluster("Compute DEKs"):
            dek_vm = Storage("VM Disk Key")
            dek_aks = Storage("AKS Secret Key")

    # Protected Resources
    with Cluster("Protected Resources", graph_attr={"bgcolor": "#D4E9D7", "style": "rounded"}):
        blob = BlobStorage("Azure Blob\nStorage")
        sql = SQLDatabases("SQL\nDatabase")
        vm = VM("Virtual\nMachines")

    # Key Hierarchy Connections
    hsm >> Edge(label="Protects", color="red", style="bold") >> root_key
    root_key >> Edge(label="Wraps", color="orange") >> kek_storage
    root_key >> Edge(color="orange") >> kek_db
    root_key >> Edge(color="orange") >> kek_compute
    root_key >> Edge(color="orange") >> kek_backup

    kek_storage >> Edge(label="Encrypts", color="blue") >> dek_blob
    kek_storage >> Edge(color="blue") >> dek_file
    kek_storage >> Edge(color="blue") >> dek_disk

    kek_db >> Edge(color="blue") >> dek_sql
    kek_db >> Edge(color="blue") >> dek_cosmos

    kek_compute >> Edge(color="blue") >> dek_vm
    kek_compute >> Edge(color="blue") >> dek_aks

    dek_blob >> Edge(label="Protects Data", color="green", style="dashed") >> blob
    dek_sql >> Edge(color="green", style="dashed") >> sql
    dek_vm >> Edge(color="green", style="dashed") >> vm

print(f"✅ Generated: {output_dir}/encryption-key-hierarchy.svg")
