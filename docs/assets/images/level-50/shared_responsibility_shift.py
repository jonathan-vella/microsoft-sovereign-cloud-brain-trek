#!/usr/bin/env python3
"""Shared Responsibility Model Shift diagram for Level 50"""
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
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(6, 3.7, 'Responsibility Shift Across Cloud Models',
            fontsize=14, fontweight='bold', ha='center', color=AZURE_DARK)

    # Boxes with gradient showing shift
    models = [
        (1.5, 'On-Premises', '100% You', '#bbdefb', AZURE_BLUE),
        (4.5, 'IaaS', 'Infrastructure\nmanaged', '#90caf9', AZURE_BLUE),
        (7.5, 'PaaS', 'Platform\nmanaged', '#a5d6a7', AZURE_GREEN),
        (10.5, 'SaaS', 'Everything\nmanaged', '#c8e6c9', AZURE_GREEN)
    ]

    for x, title, desc, color, edge in models:
        box = FancyBboxPatch((x - 1, 1), 2, 2, boxstyle="round,pad=0.05",
                              facecolor=color, edgecolor=edge, linewidth=2)
        ax.add_patch(box)
        ax.text(x, 2.6, title, fontsize=11, fontweight='bold', ha='center', color=AZURE_DARK)
        ax.text(x, 1.7, desc, fontsize=9, ha='center', va='center', color=AZURE_DARK)

    # Arrows between boxes
    for i in range(3):
        x_start = models[i][0] + 1.1
        x_end = models[i+1][0] - 1.1
        arrow = FancyArrowPatch((x_start, 2), (x_end, 2),
                                arrowstyle='-|>', mutation_scale=15,
                                fc=AZURE_DARK, ec=AZURE_DARK, linewidth=2)
        ax.add_patch(arrow)

    # Bottom legend
    ax.text(3, 0.4, '← More Customer Control', fontsize=9, ha='center', color=AZURE_BLUE)
    ax.text(9, 0.4, 'More Provider Management →', fontsize=9, ha='center', color=AZURE_GREEN)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('shared-responsibility-shift.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated shared-responsibility-shift.svg")
    plt.close(fig)
