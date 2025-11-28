#!/usr/bin/env python3
"""Azure Storage Tiers diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Color palette
AZURE_DARK = '#004578'
HOT_COLOR = '#FFE4B5'
HOT_EDGE = '#FF8C00'
COOL_COLOR = '#E0FFFF'
COOL_EDGE = '#0078D4'
COLD_COLOR = '#B0E0E6'
COLD_EDGE = '#004578'
ARCHIVE_COLOR = '#D3D3D3'
ARCHIVE_EDGE = '#666666'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 7.5, '[Storage] Azure Storage Tiers',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Define tiers
    tiers = [
        {
            'x': 1.75, 'y': 4, 'title': '🔥 Hot Tier',
            'color': HOT_COLOR, 'edge': HOT_EDGE,
            'items': ['Frequently Accessed Data', 'Lowest Access Cost', 'Higher Storage Cost']
        },
        {
            'x': 5.25, 'y': 4, 'title': '[Cool] Cool Tier',
            'color': COOL_COLOR, 'edge': COOL_EDGE,
            'items': ['Infrequent Access', '30+ Day Retention', 'Lower Storage Cost']
        },
        {
            'x': 8.75, 'y': 4, 'title': '[Cold] Cold Tier',
            'color': COLD_COLOR, 'edge': COLD_EDGE,
            'items': ['Rare Access', '90+ Day Retention', 'Even Lower Cost']
        },
        {
            'x': 12.25, 'y': 4, 'title': '[Archive] Archive Tier',
            'color': ARCHIVE_COLOR, 'edge': ARCHIVE_EDGE,
            'items': ['Offline Storage', '180+ Day Retention', 'Lowest Storage Cost', 'Hours to Rehydrate']
        }
    ]

    for tier in tiers:
        height = 4.5 if len(tier['items']) > 3 else 4
        y_offset = 0 if len(tier['items']) > 3 else 0.25

        # Background box
        box = FancyBboxPatch((tier['x'] - 1.5, tier['y'] - 2.5 + y_offset), 3, height,
                              boxstyle="round,pad=0.1",
                              facecolor=tier['color'], edgecolor=tier['edge'], linewidth=2)
        ax.add_patch(box)

        # Title
        ax.text(tier['x'], tier['y'] + 1.2 + y_offset, tier['title'],
                fontsize=10, fontweight='bold', ha='center', color=tier['edge'])

        # Items
        for i, item in enumerate(tier['items']):
            item_box = FancyBboxPatch((tier['x'] - 1.3, tier['y'] + 0.3 - i*0.65 + y_offset), 2.6, 0.55,
                                       boxstyle="round,pad=0.02", facecolor='white',
                                       edgecolor=tier['edge'], linewidth=0.5, alpha=0.9)
            ax.add_patch(item_box)
            ax.text(tier['x'], tier['y'] + 0.55 - i*0.65 + y_offset, item,
                    fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Arrows between tiers
    arrow_y = 4.8
    for i in range(3):
        x_start = tiers[i]['x'] + 1.6
        x_end = tiers[i+1]['x'] - 1.6
        arrow = FancyArrowPatch((x_start, arrow_y), (x_end, arrow_y),
                                arrowstyle='-|>', mutation_scale=12,
                                fc=AZURE_DARK, ec=AZURE_DARK, linewidth=1.5)
        ax.add_patch(arrow)

    # Labels above arrows
    ax.text(3.5, 5.2, 'Less\nFrequent', fontsize=7, ha='center', va='bottom', color=AZURE_DARK)
    ax.text(7, 5.2, 'Rarely\nNeeded', fontsize=7, ha='center', va='bottom', color=AZURE_DARK)
    ax.text(10.5, 5.2, 'Long-term', fontsize=7, ha='center', va='bottom', color=AZURE_DARK)

    # Cost/Access trade-off legend at bottom
    legend_bg = FancyBboxPatch((3, 0.3), 8, 1, boxstyle="round,pad=0.05",
                                facecolor='#F5F5F5', edgecolor=AZURE_DARK, linewidth=1)
    ax.add_patch(legend_bg)

    ax.text(7, 1.0, 'Key Trade-off', fontsize=10, fontweight='bold', ha='center', color=AZURE_DARK)
    ax.text(5, 0.6, '← Higher Access Cost', fontsize=8, ha='center', color=HOT_EDGE)
    ax.text(9, 0.6, 'Higher Storage Cost →', fontsize=8, ha='center', color=ARCHIVE_EDGE)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('azure-storage-tiers.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated azure-storage-tiers.svg")
    plt.close(fig)
