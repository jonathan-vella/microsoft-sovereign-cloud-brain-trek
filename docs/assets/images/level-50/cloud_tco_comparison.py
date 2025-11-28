#!/usr/bin/env python3
"""Cloud vs On-Premises TCO Comparison diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_RED = '#D13438'
AZURE_ORANGE = '#FF8C00'
AZURE_LIGHT = '#E8F4FD'
LIGHT_RED = '#FFE4E1'
LIGHT_GREEN = '#D4E9D7'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 7.5, 'Cloud vs On-Premises Total Cost of Ownership (TCO)',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # On-Premises box (left side)
    onprem_bg = FancyBboxPatch((0.5, 1), 5, 5.5, boxstyle="round,pad=0.1",
                                facecolor=LIGHT_RED, edgecolor=AZURE_RED, linewidth=2)
    ax.add_patch(onprem_bg)
    ax.text(3, 6.2, 'Traditional On-Premises', fontsize=12, fontweight='bold',
            ha='center', color=AZURE_RED)

    onprem_items = [
        ('Hardware Purchase', 'High', 5.3),
        ('Data Center', 'Medium', 4.6),
        ('IT Staff', 'Medium', 3.9),
        ('Power/Cooling', 'Low', 3.2),
        ('Maintenance', 'Low', 2.5),
        ('Idle Capacity', 'Medium', 1.8)
    ]

    for item, cost, y in onprem_items:
        box = FancyBboxPatch((0.8, y - 0.25), 4.4, 0.5, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_RED, linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(1, y, item, fontsize=9, ha='left', va='center', color=AZURE_DARK)
        ax.text(5, y, cost, fontsize=9, ha='right', va='center', color=AZURE_RED, fontweight='bold')

    # Cloud box (right side)
    cloud_bg = FancyBboxPatch((8.5, 1), 5, 5.5, boxstyle="round,pad=0.1",
                               facecolor=LIGHT_GREEN, edgecolor=AZURE_GREEN, linewidth=2)
    ax.add_patch(cloud_bg)
    ax.text(11, 6.2, 'Cloud Model', fontsize=12, fontweight='bold',
            ha='center', color=AZURE_GREEN)

    cloud_items = [
        ('Subscription', 'Pay-as-you-go', 5.3),
        ('Auto-scaling', 'No idle waste', 4.4),
        ('Managed Services', 'Reduced staff', 3.5),
        ('No Hardware', 'Zero CapEx', 2.6)
    ]

    for item, benefit, y in cloud_items:
        box = FancyBboxPatch((8.8, y - 0.25), 4.4, 0.5, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_GREEN, linewidth=1, alpha=0.9)
        ax.add_patch(box)
        ax.text(8.95, y, item, fontsize=9, ha='left', va='center', color=AZURE_DARK)
        ax.text(13, y, benefit, fontsize=8, ha='right', va='center', color=AZURE_GREEN, fontweight='bold')

    # Arrow showing migration
    arrow = FancyArrowPatch((5.8, 3.75), (8.2, 3.75),
                            arrowstyle='-|>', mutation_scale=20,
                            fc=AZURE_BLUE, ec=AZURE_BLUE, linewidth=3)
    ax.add_patch(arrow)
    ax.text(7, 4.1, 'Migrate', fontsize=10, fontweight='bold', ha='center', color=AZURE_BLUE)

    # Bottom note
    ax.text(7, 0.5, 'Cloud eliminates capital expenses and reduces operational overhead',
            fontsize=10, fontstyle='italic', ha='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('cloud-tco-comparison.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated cloud-tco-comparison.svg")
    plt.close(fig)
