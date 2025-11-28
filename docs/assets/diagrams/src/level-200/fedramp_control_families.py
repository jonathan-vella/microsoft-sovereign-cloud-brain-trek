#!/usr/bin/env python3
"""
FedRAMP Control Families Diagram
L200-53: Visual representation of FedRAMP control families and their relationships
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-200"
os.makedirs(output_dir, exist_ok=True)

# FedRAMP Control Families (NIST 800-53)
control_families = {
    "Access Control (AC)": {"count": 25, "category": "Technical", "color": "#0078D4"},
    "Awareness & Training (AT)": {"count": 5, "category": "Operational", "color": "#107C10"},
    "Audit & Accountability (AU)": {"count": 16, "category": "Technical", "color": "#0078D4"},
    "Assessment (CA)": {"count": 9, "category": "Management", "color": "#5C2D91"},
    "Configuration Mgmt (CM)": {"count": 11, "category": "Operational", "color": "#107C10"},
    "Contingency Planning (CP)": {"count": 13, "category": "Operational", "color": "#107C10"},
    "Identification (IA)": {"count": 12, "category": "Technical", "color": "#0078D4"},
    "Incident Response (IR)": {"count": 10, "category": "Operational", "color": "#107C10"},
    "Maintenance (MA)": {"count": 6, "category": "Operational", "color": "#107C10"},
    "Media Protection (MP)": {"count": 8, "category": "Operational", "color": "#107C10"},
    "Physical Protection (PE)": {"count": 20, "category": "Operational", "color": "#107C10"},
    "Planning (PL)": {"count": 9, "category": "Management", "color": "#5C2D91"},
    "Personnel Security (PS)": {"count": 9, "category": "Operational", "color": "#107C10"},
    "Risk Assessment (RA)": {"count": 6, "category": "Management", "color": "#5C2D91"},
    "System & Services (SA)": {"count": 22, "category": "Management", "color": "#5C2D91"},
    "System Protection (SC)": {"count": 44, "category": "Technical", "color": "#0078D4"},
    "System Integrity (SI)": {"count": 17, "category": "Technical", "color": "#0078D4"},
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
fig.suptitle("FedRAMP Control Families Overview", fontsize=18, fontweight='bold', y=0.98)

# Chart 1: Bar chart of control counts by family
families = list(control_families.keys())
counts = [v["count"] for v in control_families.values()]
colors = [v["color"] for v in control_families.values()]

y_pos = np.arange(len(families))
bars = ax1.barh(y_pos, counts, color=colors, edgecolor='white', linewidth=0.5)

ax1.set_yticks(y_pos)
ax1.set_yticklabels(families, fontsize=9)
ax1.set_xlabel("Number of Controls", fontsize=11)
ax1.set_title("Controls per Family", fontsize=14, fontweight='bold', pad=10)
ax1.invert_yaxis()

# Add count labels
for bar, count in zip(bars, counts):
    ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             str(count), va='center', fontsize=9)

ax1.set_xlim(0, max(counts) + 5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Chart 2: Pie chart by category
categories = {}
for family, data in control_families.items():
    cat = data["category"]
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += data["count"]

cat_colors = {"Technical": "#0078D4", "Operational": "#107C10", "Management": "#5C2D91"}
wedges, texts, autotexts = ax2.pie(
    categories.values(),
    labels=categories.keys(),
    autopct=lambda pct: f'{int(pct/100*sum(categories.values()))}\n({pct:.0f}%)',
    colors=[cat_colors[c] for c in categories.keys()],
    startangle=90,
    explode=[0.02] * len(categories),
    textprops={'fontsize': 11}
)
ax2.set_title("Controls by Category", fontsize=14, fontweight='bold', pad=10)

# Legend
legend_patches = [
    mpatches.Patch(color="#0078D4", label="Technical Controls"),
    mpatches.Patch(color="#107C10", label="Operational Controls"),
    mpatches.Patch(color="#5C2D91", label="Management Controls"),
]
fig.legend(handles=legend_patches, loc='lower center', ncol=3, fontsize=10,
           frameon=True, fancybox=True, shadow=True, bbox_to_anchor=(0.5, 0.02))

# FedRAMP Impact Levels annotation
info_text = """
FedRAMP Impact Levels:
• Low: 125 controls (Low sensitivity)
• Moderate: 325 controls (Serious impact)
• High: 421 controls (Catastrophic impact)
"""
fig.text(0.02, 0.02, info_text, fontsize=9, verticalalignment='bottom',
         bbox=dict(boxstyle='round', facecolor='#F0F0F0', alpha=0.8))

plt.tight_layout(rect=[0, 0.08, 1, 0.96])

# Save
output_path = f"{output_dir}/fedramp-control-families"
plt.savefig(f"{output_path}.svg", format='svg', dpi=150, bbox_inches='tight')
plt.savefig(f"{output_path}.png", format='png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✅ Generated: {output_path}.svg")
print(f"✅ Generated: {output_path}.png")
