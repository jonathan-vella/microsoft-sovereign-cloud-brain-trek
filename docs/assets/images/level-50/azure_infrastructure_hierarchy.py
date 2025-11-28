#!/usr/bin/env python3
"""Azure Infrastructure Hierarchy diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_LIGHT = '#E8F4FD'

def create_diagram():
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(6, 8.5, '[World] Azure Global Infrastructure Hierarchy',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Main container
    main_bg = FancyBboxPatch((0.5, 0.5), 11, 7.5, boxstyle="round,pad=0.1",
                              facecolor=AZURE_LIGHT, edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(main_bg)

    # Geography level (top)
    geo = FancyBboxPatch((4.5, 6.5), 3, 1, boxstyle="round,pad=0.02",
                          facecolor='#bbdefb', edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(geo)
    ax.text(6, 7, 'Geography', fontsize=11, fontweight='bold', ha='center', va='center', color=AZURE_DARK)

    # Region level
    regions = [
        (3, 4.8, 'Region 1'),
        (9, 4.8, 'Region 2')
    ]

    for x, y, label in regions:
        box = FancyBboxPatch((x - 1.2, y - 0.4), 2.4, 0.8, boxstyle="round,pad=0.02",
                              facecolor='#90caf9', edgecolor=AZURE_BLUE, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=10, fontweight='bold', ha='center', va='center', color=AZURE_DARK)

    # Arrows from Geography to Regions
    ax.annotate('', xy=(3, 5.2), xytext=(5.2, 6.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))
    ax.annotate('', xy=(9, 5.2), xytext=(6.8, 6.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # Availability Zones (under Region 1)
    azs = [
        (1.5, 3, 'AZ 1'),
        (3, 3, 'AZ 2'),
        (4.5, 3, 'AZ 3')
    ]

    for x, y, label in azs:
        box = FancyBboxPatch((x - 0.7, y - 0.35), 1.4, 0.7, boxstyle="round,pad=0.02",
                              facecolor='#a5d6a7', edgecolor=AZURE_GREEN, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=9, fontweight='bold', ha='center', va='center', color=AZURE_DARK)

    # Arrows from Region 1 to AZs
    for x, y, _ in azs:
        ax.annotate('', xy=(x, y + 0.35), xytext=(3, 4.4),
                    arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1.5))

    # Data Centers (under each AZ)
    dcs = [
        (1.5, 1.5, 'DC'),
        (3, 1.5, 'DC'),
        (4.5, 1.5, 'DC')
    ]

    for i, (x, y, label) in enumerate(dcs):
        box = FancyBboxPatch((x - 0.6, y - 0.35), 1.2, 0.7, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_DARK, linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, f'Data\nCenter', fontsize=7, ha='center', va='center', color=AZURE_DARK)

        # Arrow from AZ to DC
        ax.annotate('', xy=(x, y + 0.35), xytext=(x, 2.65),
                    arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1))

    # Legend on the right side
    legend_items = [
        (9, 3.5, 'Geography', '#bbdefb', AZURE_BLUE, 'Regulatory boundary'),
        (9, 2.7, 'Region', '#90caf9', AZURE_BLUE, 'Data center cluster'),
        (9, 1.9, 'Avail Zone', '#a5d6a7', AZURE_GREEN, 'Fault isolation'),
        (9, 1.1, 'Data Center', 'white', AZURE_DARK, 'Physical facility')
    ]

    for x, y, label, color, edge, desc in legend_items:
        box = FancyBboxPatch((x - 0.8, y - 0.2), 1.6, 0.4, boxstyle="round,pad=0.02",
                              facecolor=color, edgecolor=edge, linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=8, ha='center', va='center', color=AZURE_DARK)
        ax.text(x + 1.5, y, desc, fontsize=8, ha='left', va='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('azure-infrastructure-hierarchy.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated azure-infrastructure-hierarchy.svg")
    plt.close(fig)
