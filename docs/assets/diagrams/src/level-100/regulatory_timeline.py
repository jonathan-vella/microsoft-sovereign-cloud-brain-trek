#!/usr/bin/env python3
"""
Regulatory Compliance Timeline
Shows the evolution of data sovereignty regulations.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_RED = '#D13438'
AZURE_PURPLE = '#5C2D91'


def create_regulatory_timeline():
    """Create a timeline of major data sovereignty regulations."""

    fig, ax = plt.subplots(figsize=(16, 8))

    # Regulations with dates and details
    regulations = [
        {
            'year': 2011, 'name': 'FedRAMP',
            'region': 'US', 'color': AZURE_BLUE,
            'description': 'Federal cloud security\nstandard established'
        },
        {
            'year': 2013, 'name': 'HIPAA Omnibus',
            'region': 'US', 'color': AZURE_GREEN,
            'description': 'Healthcare data\nrequirements expanded'
        },
        {
            'year': 2016, 'name': 'GDPR Adopted',
            'region': 'EU', 'color': AZURE_PURPLE,
            'description': 'General Data Protection\nRegulation adopted'
        },
        {
            'year': 2018, 'name': 'GDPR Effective',
            'region': 'EU', 'color': AZURE_PURPLE,
            'description': 'GDPR enforcement begins\n€20M/4% fines'
        },
        {
            'year': 2020, 'name': 'Schrems II',
            'region': 'EU', 'color': AZURE_RED,
            'description': 'Privacy Shield\ninvalidated by ECJ'
        },
        {
            'year': 2021, 'name': 'China PIPL',
            'region': 'APAC', 'color': AZURE_ORANGE,
            'description': 'Personal Information\nProtection Law'
        },
        {
            'year': 2022, 'name': 'EU Data Act',
            'region': 'EU', 'color': AZURE_PURPLE,
            'description': 'Data portability and\ncloud switching rules'
        },
        {
            'year': 2023, 'name': 'EU-US DPF',
            'region': 'EU/US', 'color': AZURE_GREEN,
            'description': 'Data Privacy Framework\nreplaces Privacy Shield'
        },
        {
            'year': 2024, 'name': 'EU AI Act',
            'region': 'EU', 'color': AZURE_PURPLE,
            'description': 'AI system regulation\nwith sovereignty aspects'
        },
        {
            'year': 2025, 'name': 'DORA',
            'region': 'EU', 'color': AZURE_ORANGE,
            'description': 'Digital Operational\nResilience Act effective'
        },
    ]

    # Timeline parameters
    y_center = 4
    timeline_height = 0.3
    year_range = (2010, 2026)

    # Draw main timeline
    ax.fill_between([year_range[0], year_range[1]], y_center - timeline_height,
                    y_center + timeline_height, color='#E0E0E0')

    # Year markers
    for year in range(2010, 2027, 2):
        ax.axvline(x=year, color='#CCCCCC', linewidth=0.5, linestyle='-')
        ax.text(year, y_center - 0.8, str(year), ha='center', va='top',
                fontsize=9, color='#666666')

    # Plot regulations
    for i, reg in enumerate(regulations):
        y_offset = 1.5 if i % 2 == 0 else -1.5
        y_pos = y_center + y_offset

        # Marker on timeline
        ax.scatter(reg['year'], y_center, s=150, c=reg['color'],
                   edgecolors='white', linewidths=2, zorder=10)

        # Connecting line
        ax.plot([reg['year'], reg['year']], [y_center, y_pos - 0.3 * np.sign(y_offset)],
                color=reg['color'], linewidth=2, linestyle='-')

        # Info box
        box_height = 1.2
        box_width = 1.8
        box_y = y_pos + (0.3 if y_offset > 0 else -box_height - 0.3)

        rect = mpatches.FancyBboxPatch(
            (reg['year'] - box_width/2, box_y), box_width, box_height,
            boxstyle="round,pad=0.1", facecolor=reg['color'],
            edgecolor='white', linewidth=2, alpha=0.9
        )
        ax.add_patch(rect)

        # Regulation name
        ax.text(reg['year'], box_y + box_height - 0.25, reg['name'],
                ha='center', va='top', fontsize=10, fontweight='bold', color='white')

        # Region badge
        ax.text(reg['year'], box_y + box_height - 0.5, f"[{reg['region']}]",
                ha='center', va='top', fontsize=8, color='white', alpha=0.8)

        # Description
        ax.text(reg['year'], box_y + 0.25, reg['description'],
                ha='center', va='bottom', fontsize=7, color='white')

    # Title
    ax.text((year_range[0] + year_range[1]) / 2, 7.5,
            'Data Sovereignty Regulatory Timeline',
            ha='center', va='center', fontsize=16, fontweight='bold',
            color=AZURE_DARK_BLUE)

    ax.text((year_range[0] + year_range[1]) / 2, 7.0,
            'Key regulations driving cloud sovereignty requirements worldwide',
            ha='center', va='center', fontsize=11, color='#666666', style='italic')

    # Region legend
    legend_elements = [
        mpatches.Patch(facecolor=AZURE_BLUE, edgecolor='white', label='US Federal'),
        mpatches.Patch(facecolor=AZURE_PURPLE, edgecolor='white', label='European Union'),
        mpatches.Patch(facecolor=AZURE_ORANGE, edgecolor='white', label='Global/APAC'),
        mpatches.Patch(facecolor=AZURE_GREEN, edgecolor='white', label='Cross-border'),
        mpatches.Patch(facecolor=AZURE_RED, edgecolor='white', label='Landmark Ruling'),
    ]
    ax.legend(handles=legend_elements, loc='lower center', ncol=5, fontsize=9,
              framealpha=0.95, bbox_to_anchor=(0.5, -0.05))

    # Set limits
    ax.set_xlim(year_range[0] - 0.5, year_range[1] + 0.5)
    ax.set_ylim(0, 8)
    ax.axis('off')

    return fig


def main():
    """Generate and save the regulatory timeline."""

    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Regulatory Compliance Timeline...")

    fig = create_regulatory_timeline()

    output_path = output_dir / 'regulatory-timeline.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)
    print("✅ Timeline generated successfully!")


if __name__ == '__main__':
    main()
