#!/usr/bin/env python3
"""
Security Patterns Matrix
L200-52: Security implementation patterns for sovereign cloud
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
os.makedirs(output_dir, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(16, 10))
fig.suptitle("Security Patterns for Sovereign Cloud Environments", fontsize=16, fontweight='bold', y=0.98)

# Chart 1: Security Controls Matrix
ax1 = axes[0]
ax1.set_title("Security Controls by Layer", fontsize=12, fontweight='bold', pad=10)

layers = ["Identity", "Network", "Compute", "Data", "Application"]
controls = [
    "MFA / Passwordless",
    "Conditional Access",
    "Privileged Identity Mgmt",
    "Network Segmentation",
    "Private Endpoints",
    "Firewall / NSG",
    "VM Hardening",
    "Just-In-Time Access",
    "Confidential Compute",
    "Encryption at Rest",
    "Encryption in Transit",
    "Key Management (CMK)",
    "WAF / DDoS Protection",
    "Code Scanning",
    "API Security",
]

# Implementation level by environment (0-100%)
public_cloud = [95, 90, 85, 80, 95, 90, 75, 90, 60, 95, 95, 90, 95, 80, 85]
sovereign_cloud = [98, 95, 95, 95, 98, 95, 90, 95, 80, 98, 98, 98, 95, 90, 90]
azure_local = [90, 85, 90, 90, 85, 90, 95, 85, 70, 95, 95, 95, 80, 85, 85]

x = np.arange(len(controls))
width = 0.25

bars1 = ax1.barh(x - width, public_cloud, width, label='Public Cloud', color='#0078D4', alpha=0.8)
bars2 = ax1.barh(x, sovereign_cloud, width, label='Sovereign Cloud', color='#5C2D91', alpha=0.8)
bars3 = ax1.barh(x + width, azure_local, width, label='Azure Local', color='#107C10', alpha=0.8)

ax1.set_yticks(x)
ax1.set_yticklabels(controls, fontsize=9)
ax1.set_xlabel('Implementation Level (%)', fontsize=10)
ax1.set_xlim(0, 105)
ax1.legend(loc='lower right', fontsize=9)
ax1.axvline(x=90, color='#FF8C00', linestyle='--', alpha=0.7, label='Target')
ax1.invert_yaxis()

# Add layer separators
layer_positions = [3, 6, 9, 12, 15]
layer_labels = ["Identity", "Network", "Compute", "Data", "Application"]
for i, (pos, label) in enumerate(zip(layer_positions, layer_labels)):
    if i < len(layer_positions) - 1:
        ax1.axhline(y=pos - 0.5, color='gray', linestyle='-', alpha=0.3)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Chart 2: Compliance Requirements Heat Map
ax2 = axes[1]
ax2.set_title("Security Requirements by Compliance Framework", fontsize=12, fontweight='bold', pad=10)
ax2.axis('off')

frameworks = ["GDPR", "HIPAA", "FedRAMP\nHigh", "PCI\nDSS", "SOC 2", "ISO\n27001"]
requirements = [
    "Data Residency",
    "Encryption (Rest)",
    "Encryption (Transit)",
    "Access Logging",
    "MFA Required",
    "Key Management",
    "Incident Response",
    "Pen Testing",
    "Vulnerability Scan",
    "Data Classification",
]

# Requirement levels: 3=Required, 2=Recommended, 1=Optional, 0=N/A
req_matrix = np.array([
    [3, 2, 3, 2, 2, 2],  # Data Residency
    [3, 3, 3, 3, 3, 3],  # Encryption Rest
    [3, 3, 3, 3, 3, 3],  # Encryption Transit
    [3, 3, 3, 3, 3, 3],  # Access Logging
    [2, 3, 3, 3, 3, 3],  # MFA
    [3, 3, 3, 3, 2, 3],  # Key Management
    [3, 3, 3, 3, 3, 3],  # Incident Response
    [1, 2, 3, 3, 2, 2],  # Pen Testing
    [2, 3, 3, 3, 3, 3],  # Vuln Scan
    [3, 3, 3, 3, 2, 3],  # Data Classification
])

# Color mapping
colors = []
for row in req_matrix:
    row_colors = []
    for val in row:
        if val == 3:
            row_colors.append('#D13438')  # Required - Red
        elif val == 2:
            row_colors.append('#FF8C00')  # Recommended - Orange
        elif val == 1:
            row_colors.append('#FFF4E6')  # Optional - Light
        else:
            row_colors.append('#F5F5F5')  # N/A - Gray
    colors.append(row_colors)

# Create text labels
text_labels = []
for row in req_matrix:
    row_text = []
    for val in row:
        if val == 3:
            row_text.append('●')
        elif val == 2:
            row_text.append('◐')
        elif val == 1:
            row_text.append('○')
        else:
            row_text.append('-')
    text_labels.append(row_text)

table = ax2.table(
    cellText=text_labels,
    rowLabels=requirements,
    colLabels=frameworks,
    cellColours=colors,
    rowColours=['#E8F4FD'] * len(requirements),
    colColours=['#E8F4FD'] * len(frameworks),
    cellLoc='center',
    loc='center',
    bbox=[0.1, 0.15, 0.85, 0.8]
)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#D13438', edgecolor='black', label='● Required'),
    mpatches.Patch(facecolor='#FF8C00', edgecolor='black', label='◐ Recommended'),
    mpatches.Patch(facecolor='#FFF4E6', edgecolor='black', label='○ Optional'),
]
ax2.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=10,
           bbox_to_anchor=(0.5, 0.02))

plt.tight_layout(rect=[0, 0.02, 1, 0.96])

# Save
output_path = f"{output_dir}/security-patterns-matrix"
plt.savefig(f"{output_path}.svg", format='svg', dpi=150, bbox_inches='tight')
plt.savefig(f"{output_path}.png", format='png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✅ Generated: {output_path}.svg")
print(f"✅ Generated: {output_path}.png")
