#!/usr/bin/env python3
"""Azure Networking Fundamentals diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_ORANGE = '#FF8C00'
AZURE_GREEN = '#107C10'
AZURE_LIGHT = '#E8F4FD'
LIGHT_ORANGE = '#FFF4E6'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 9.5, '[Cloud] Azure Networking Fundamentals',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Internet icon
    internet = Circle((1.5, 7), 0.8, facecolor='white', edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(internet)
    ax.text(1.5, 7, '[Global]\nInternet', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Azure section
    azure_bg = FancyBboxPatch((3.5, 3), 7, 6, boxstyle="round,pad=0.1",
                               facecolor=AZURE_LIGHT, edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(azure_bg)
    ax.text(7, 8.7, '[Cloud] Azure Networking', fontsize=12, fontweight='bold',
            ha='center', color=AZURE_BLUE)

    # Application Gateway
    agw = FancyBboxPatch((4.5, 7), 2, 1, boxstyle="round,pad=0.02",
                          facecolor=AZURE_BLUE, edgecolor=AZURE_DARK, linewidth=1.5)
    ax.add_patch(agw)
    ax.text(5.5, 7.5, 'Application\nGateway', fontsize=8, ha='center', va='center', color='white')

    # Load Balancer
    lb = FancyBboxPatch((4.5, 5.5), 2, 1, boxstyle="round,pad=0.02",
                         facecolor=AZURE_BLUE, edgecolor=AZURE_DARK, linewidth=1.5)
    ax.add_patch(lb)
    ax.text(5.5, 6, 'Load\nBalancer', fontsize=8, ha='center', va='center', color='white')

    # VNet section
    vnet_bg = FancyBboxPatch((7, 4), 3.2, 4, boxstyle="round,pad=0.1",
                              facecolor='white', edgecolor=AZURE_DARK, linewidth=2)
    ax.add_patch(vnet_bg)
    ax.text(8.6, 7.7, 'Virtual Network (VNet)', fontsize=9, fontweight='bold',
            ha='center', color=AZURE_DARK)

    # Subnet A
    subnet_a = FancyBboxPatch((7.2, 6.2), 2.8, 1.2, boxstyle="round,pad=0.02",
                               facecolor='#E8F4FD', edgecolor=AZURE_BLUE, linewidth=1)
    ax.add_patch(subnet_a)
    ax.text(8.6, 6.8, 'Subnet A\n10.0.1.0/24', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Subnet B
    subnet_b = FancyBboxPatch((7.2, 4.5), 2.8, 1.2, boxstyle="round,pad=0.02",
                               facecolor='#E8F4FD', edgecolor=AZURE_BLUE, linewidth=1)
    ax.add_patch(subnet_b)
    ax.text(8.6, 5.1, 'Subnet B\n10.0.2.0/24', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # NSG
    nsg = FancyBboxPatch((4.5, 4), 2, 1, boxstyle="round,pad=0.02",
                          facecolor=AZURE_ORANGE, edgecolor=AZURE_DARK, linewidth=1.5)
    ax.add_patch(nsg)
    ax.text(5.5, 4.5, 'Network Security\nGroup', fontsize=8, ha='center', va='center', color='white')

    # Azure Firewall
    fw = FancyBboxPatch((4, 3.2), 2, 0.6, boxstyle="round,pad=0.02",
                         facecolor='#D13438', edgecolor=AZURE_DARK, linewidth=1.5)
    ax.add_patch(fw)
    ax.text(5, 3.5, 'Azure Firewall', fontsize=8, ha='center', va='center', color='white')

    # On-Premises section
    onprem_bg = FancyBboxPatch((11, 4), 2.5, 4, boxstyle="round,pad=0.1",
                                facecolor=LIGHT_ORANGE, edgecolor=AZURE_ORANGE, linewidth=2)
    ax.add_patch(onprem_bg)
    ax.text(12.25, 7.7, '[Building] On-Premises', fontsize=10, fontweight='bold',
            ha='center', color=AZURE_ORANGE)

    # Data Center
    dc = FancyBboxPatch((11.25, 5), 2, 1.5, boxstyle="round,pad=0.02",
                         facecolor='white', edgecolor=AZURE_ORANGE, linewidth=1.5)
    ax.add_patch(dc)
    ax.text(12.25, 5.75, 'Data Center', fontsize=9, ha='center', va='center', color=AZURE_DARK)

    # Connection arrows
    # Internet to App Gateway
    ax.annotate('', xy=(4.5, 7.5), xytext=(2.3, 7),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # App Gateway to Load Balancer
    ax.annotate('', xy=(5.5, 6.5), xytext=(5.5, 7),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # Load Balancer to Subnets
    ax.annotate('', xy=(7.2, 6.8), xytext=(6.5, 6),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))
    ax.annotate('', xy=(7.2, 5.1), xytext=(6.5, 5.8),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # NSG to Subnets (dashed)
    ax.plot([6.5, 7.2], [4.5, 6.5], 'k--', lw=1, alpha=0.5)
    ax.plot([6.5, 7.2], [4.5, 5.1], 'k--', lw=1, alpha=0.5)
    ax.text(6.2, 5.5, 'Rules', fontsize=7, color=AZURE_DARK, alpha=0.7)

    # VPN/ExpressRoute connection
    ax.annotate('', xy=(11, 6), xytext=(10.2, 6),
                arrowprops=dict(arrowstyle='<->', color=AZURE_ORANGE, lw=2))
    ax.text(10.6, 6.5, 'VPN/\nExpressRoute', fontsize=7, ha='center', color=AZURE_ORANGE)

    # Firewall to VNet
    ax.annotate('', xy=(7, 5), xytext=(6, 3.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1.5))

    # Legend at bottom
    legend_bg = FancyBboxPatch((0.5, 0.3), 13, 2.2, boxstyle="round,pad=0.1",
                                facecolor='#F5F5F5', edgecolor=AZURE_DARK, linewidth=1)
    ax.add_patch(legend_bg)

    ax.text(7, 2.2, 'Key Components', fontsize=11, fontweight='bold', ha='center', color=AZURE_DARK)

    components = [
        (2, 'VNet', 'Isolated network', AZURE_BLUE),
        (5, 'Subnets', 'IP segmentation', AZURE_BLUE),
        (8, 'NSG', 'Traffic rules', AZURE_ORANGE),
        (11, 'Firewall', 'Security filtering', '#D13438')
    ]

    for x, name, desc, color in components:
        ax.text(x, 1.5, name, fontsize=9, fontweight='bold', ha='center', color=color)
        ax.text(x, 1.0, desc, fontsize=8, ha='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('azure-networking-fundamentals.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated azure-networking-fundamentals.svg")
    plt.close(fig)
