#!/usr/bin/env python3
"""
Sovereign Cloud Models Comparison
L100-33: Compare different sovereign cloud deployment models
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-100"
os.makedirs(output_dir, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle("Sovereign Cloud Deployment Models Comparison", fontsize=16, fontweight='bold', y=0.98)

# Data for comparison
models = [
    "Public Cloud\n(Standard)",
    "Sovereign\nPublic Cloud",
    "National\nPartner Cloud",
    "Azure Local\n(Connected)",
    "Azure Local\n(Disconnected)"
]

categories = {
    "Data Residency": [3, 5, 5, 5, 5],
    "Operational Control": [2, 3, 4, 4, 5],
    "Cloud Services": [5, 4, 4, 3, 2],
    "Air-Gap Capable": [1, 1, 2, 3, 5],
    "Cost Efficiency": [5, 4, 3, 3, 2],
}

# Chart 1: Radar/Spider chart
ax1 = axes[0]
ax1.set_title("Capability Comparison (Spider Chart)", fontsize=12, fontweight='bold', pad=20)

# Number of variables
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop

# Colors for each model
colors = ['#0078D4', '#5C2D91', '#FF8C00', '#107C10', '#D13438']

ax1 = fig.add_subplot(121, projection='polar')
ax1.set_theta_offset(np.pi / 2)
ax1.set_theta_direction(-1)

# Draw one axis per variable
plt.xticks(angles[:-1], categories.keys(), size=9)
ax1.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=8)
plt.ylim(0, 5)

# Plot each model
for i, model in enumerate(models):
    values = [categories[cat][i] for cat in categories.keys()]
    values += values[:1]
    ax1.plot(angles, values, 'o-', linewidth=2, label=model.replace('\n', ' '), color=colors[i])
    ax1.fill(angles, values, alpha=0.1, color=colors[i])

ax1.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=9)

# Chart 2: Use Case Matrix
ax2 = axes[1]
ax2.set_title("Use Case Suitability Matrix", fontsize=12, fontweight='bold', pad=10)
ax2.axis('off')

use_cases = [
    "General Enterprise",
    "EU Data Residency",
    "Government (Moderate)",
    "Government (High)",
    "Critical Infrastructure",
    "Air-Gapped / SCIF",
    "Edge / Remote Sites",
    "Development / Test",
]

# Suitability scores (1-5)
suitability = np.array([
    [5, 3, 2, 2, 2],  # General Enterprise
    [2, 5, 5, 4, 4],  # EU Data Residency
    [2, 4, 5, 4, 3],  # Government Moderate
    [1, 2, 4, 4, 5],  # Government High
    [1, 2, 3, 4, 5],  # Critical Infrastructure
    [1, 1, 1, 2, 5],  # Air-Gapped
    [3, 2, 2, 5, 5],  # Edge / Remote
    [5, 4, 3, 4, 3],  # Dev / Test
])

# Create heatmap-style table
cell_colors = []
for row in suitability:
    row_colors = []
    for val in row:
        if val >= 4:
            row_colors.append('#C8E6C9')  # Green
        elif val >= 3:
            row_colors.append('#FFF9C4')  # Yellow
        else:
            row_colors.append('#FFCDD2')  # Red
    cell_colors.append(row_colors)

short_models = ["Public", "Sov Public", "National", "Connected", "Disconnected"]

table = ax2.table(
    cellText=suitability,
    rowLabels=use_cases,
    colLabels=short_models,
    cellColours=cell_colors,
    rowColours=['#E8F4FD'] * len(use_cases),
    colColours=['#E8F4FD'] * len(short_models),
    cellLoc='center',
    loc='center',
    bbox=[0.1, 0.1, 0.85, 0.85]
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.8)

# Legend for suitability
legend_elements = [
    mpatches.Patch(facecolor='#C8E6C9', edgecolor='black', label='Excellent (4-5)'),
    mpatches.Patch(facecolor='#FFF9C4', edgecolor='black', label='Suitable (3)'),
    mpatches.Patch(facecolor='#FFCDD2', edgecolor='black', label='Limited (1-2)'),
]
ax2.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=9,
           bbox_to_anchor=(0.5, -0.02))

plt.tight_layout(rect=[0, 0.02, 1, 0.96])

# Save
output_path = f"{output_dir}/sovereign-cloud-models-comparison"
plt.savefig(f"{output_path}.svg", format='svg', dpi=150, bbox_inches='tight')
plt.savefig(f"{output_path}.png", format='png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✅ Generated: {output_path}.svg")
print(f"✅ Generated: {output_path}.png")
