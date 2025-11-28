#!/usr/bin/env python3
"""
Generate Compliance Frameworks Comparison Chart.
Shows key compliance frameworks and their scope/requirements.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "images" / "level-50"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Compliance frameworks data
frameworks = {
    "SOC 2": {"region": "Global", "industry": "All", "focus": "Security Controls", "color": "#0078D4"},
    "ISO 27001": {"region": "Global", "industry": "All", "focus": "ISMS", "color": "#00BCF2"},
    "GDPR": {"region": "EU", "industry": "All", "focus": "Data Privacy", "color": "#773ADC"},
    "HIPAA": {"region": "US", "industry": "Healthcare", "focus": "PHI Protection", "color": "#107C10"},
    "PCI DSS": {"region": "Global", "industry": "Payment", "focus": "Card Data", "color": "#E3008C"},
    "FedRAMP": {"region": "US", "industry": "Government", "focus": "Cloud Security", "color": "#FF8C00"},
}

# Compliance areas (simplified scoring 1-5)
areas = ["Data Protection", "Access Control", "Audit Logging", "Encryption", "Incident Response"]
scores = {
    "SOC 2": [5, 5, 5, 4, 4],
    "ISO 27001": [5, 5, 4, 5, 5],
    "GDPR": [5, 4, 4, 5, 3],
    "HIPAA": [5, 5, 5, 5, 5],
    "PCI DSS": [5, 5, 5, 5, 4],
    "FedRAMP": [5, 5, 5, 5, 5],
}

def create_comparison_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: Framework overview table-style
    ax1.axis('off')

    # Table data
    table_data = [["Framework", "Region", "Industry", "Primary Focus"]]
    colors = [["#f0f0f0"] * 4]

    for name, info in frameworks.items():
        table_data.append([name, info["region"], info["industry"], info["focus"]])
        colors.append([info["color"] + "40", "#ffffff", "#ffffff", "#ffffff"])

    table = ax1.table(
        cellText=table_data,
        cellColours=colors,
        cellLoc='center',
        loc='center',
        colWidths=[0.25, 0.2, 0.25, 0.3]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)

    # Style header row
    for i in range(4):
        table[(0, i)].set_text_props(fontweight='bold')
        table[(0, i)].set_facecolor('#333333')
        table[(0, i)].set_text_props(color='white')

    ax1.set_title("Compliance Frameworks Overview", fontsize=14, fontweight='bold', pad=20)

    # Right: Radar chart for control areas
    angles = np.linspace(0, 2 * np.pi, len(areas), endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle

    ax2 = fig.add_subplot(122, polar=True)

    for name, score in list(scores.items())[:4]:  # Show top 4
        values = score + score[:1]
        color = frameworks[name]["color"]
        ax2.plot(angles, values, 'o-', linewidth=2, label=name, color=color)
        ax2.fill(angles, values, alpha=0.15, color=color)

    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(areas, size=9)
    ax2.set_ylim(0, 5)
    ax2.set_yticks([1, 2, 3, 4, 5])
    ax2.set_yticklabels(['1', '2', '3', '4', '5'], size=8)
    ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=9)
    ax2.set_title("Control Area Coverage", fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()

    # Save
    output_file = OUTPUT_DIR / "compliance-frameworks-comparison.svg"
    plt.savefig(output_file, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none', dpi=150)
    plt.savefig(OUTPUT_DIR / "compliance-frameworks-comparison.png", format='png',
                bbox_inches='tight', facecolor='white', edgecolor='none', dpi=150)

    print(f"✅ Generated: {output_file}")
    plt.close()

if __name__ == "__main__":
    create_comparison_chart()
