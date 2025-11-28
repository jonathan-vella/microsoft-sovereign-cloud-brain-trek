#!/usr/bin/env python3
"""Cloud Scalability Patterns diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_LIGHT = '#E8F4FD'
LIGHT_ORANGE = '#FFF4E6'
LIGHT_GREEN = '#D4E9D7'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 9.5, '[Cloud] Cloud Scaling Patterns',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Vertical Scaling section (left)
    vert_bg = FancyBboxPatch((0.5, 5.5), 4, 3.5, boxstyle="round,pad=0.1",
                              facecolor=AZURE_LIGHT, edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(vert_bg)
    ax.text(2.5, 8.7, '[Up] Vertical Scaling', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_BLUE)

    # VMs increasing in size
    vm_sizes = [
        (1.3, 7.5, 0.6, 'Small\n2 CPU, 4GB'),
        (2.5, 7.0, 0.9, 'Medium\n4 CPU, 16GB'),
        (3.7, 6.3, 1.2, 'Large\n16 CPU, 64GB')
    ]

    for i, (x, y, size, label) in enumerate(vm_sizes):
        box = FancyBboxPatch((x - size/2, y - size/2), size, size,
                              boxstyle="round,pad=0.02", facecolor='white',
                              edgecolor=AZURE_BLUE, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=7, ha='center', va='center', color=AZURE_DARK)
        if i < len(vm_sizes) - 1:
            ax.annotate('', xy=(vm_sizes[i+1][0] - 0.5, vm_sizes[i+1][1]),
                       xytext=(x + size/2 + 0.1, y),
                       arrowprops=dict(arrowstyle='->', color=AZURE_BLUE, lw=2))

    # Horizontal Scaling section (right)
    horiz_bg = FancyBboxPatch((5, 5.5), 4.5, 3.5, boxstyle="round,pad=0.1",
                               facecolor=LIGHT_ORANGE, edgecolor=AZURE_ORANGE, linewidth=2)
    ax.add_patch(horiz_bg)
    ax.text(7.25, 8.7, '[H] Horizontal Scaling', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_ORANGE)

    # Load Balancer
    lb = FancyBboxPatch((6.5, 7.5), 1.5, 0.6, boxstyle="round,pad=0.02",
                         facecolor=AZURE_ORANGE, edgecolor=AZURE_DARK, linewidth=1.5)
    ax.add_patch(lb)
    ax.text(7.25, 7.8, 'Load\nBalancer', fontsize=7, ha='center', va='center', color='white')

    # Multiple instances
    for i, x in enumerate([5.5, 6.5, 7.5, 8.5]):
        box = FancyBboxPatch((x, 6.0), 0.8, 0.8, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_ORANGE, linewidth=1.5)
        ax.add_patch(box)
        label = f'N...' if i == 3 else f'{i+1}'
        ax.text(x + 0.4, 6.4, f'Instance\n{label}', fontsize=6, ha='center', va='center')
        ax.plot([7.25, x + 0.4], [7.5, 6.8], 'k-', lw=1, alpha=0.5)

    # Auto-Scaling section (bottom)
    auto_bg = FancyBboxPatch((10, 5.5), 3.5, 3.5, boxstyle="round,pad=0.1",
                              facecolor=LIGHT_GREEN, edgecolor=AZURE_GREEN, linewidth=2)
    ax.add_patch(auto_bg)
    ax.text(11.75, 8.7, '[Auto] Auto-Scaling', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_GREEN)

    # Auto-scaling states
    states = [
        (10.5, 7.5, 'Low Demand\n2 instances'),
        (11.75, 6.7, 'Medium\n5 instances'),
        (13, 7.5, 'Peak\n10 instances')
    ]

    for x, y, label in states:
        box = FancyBboxPatch((x - 0.5, y - 0.35), 1, 0.7, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_GREEN, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=7, ha='center', va='center', color=AZURE_DARK)

    # Arrows between states
    ax.annotate('', xy=(11.25, 6.8), xytext=(10.9, 7.3),
               arrowprops=dict(arrowstyle='->', color=AZURE_GREEN, lw=1.5))
    ax.text(10.7, 7.0, '↑', fontsize=8, color=AZURE_GREEN)

    ax.annotate('', xy=(12.5, 7.3), xytext=(12.25, 6.8),
               arrowprops=dict(arrowstyle='->', color=AZURE_GREEN, lw=1.5))
    ax.text(12.6, 7.0, '↑', fontsize=8, color=AZURE_GREEN)

    ax.annotate('', xy=(12.25, 6.5), xytext=(12.5, 7.1),
               arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1, ls='--'))
    ax.annotate('', xy=(10.9, 7.1), xytext=(11.25, 6.5),
               arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1, ls='--'))

    # Key Benefits section (bottom)
    benefits_bg = FancyBboxPatch((0.5, 0.5), 13, 4.5, boxstyle="round,pad=0.1",
                                  facecolor='#F5F5F5', edgecolor=AZURE_DARK, linewidth=1)
    ax.add_patch(benefits_bg)

    ax.text(7, 4.6, 'Key Benefits', fontsize=12, fontweight='bold', ha='center', color=AZURE_DARK)

    benefits = [
        (2.5, 'Vertical', ['Scale up/down CPU & RAM', 'Simple implementation', 'Limited by hardware max'], AZURE_BLUE),
        (7, 'Horizontal', ['Add/remove instances', 'Better fault tolerance', 'Requires load balancing'], AZURE_ORANGE),
        (11.5, 'Auto-Scaling', ['Automatic adjustments', 'Cost optimization', 'Handles traffic spikes'], AZURE_GREEN)
    ]

    for x, title, items, color in benefits:
        ax.text(x, 3.9, title, fontsize=10, fontweight='bold', ha='center', color=color)
        for i, item in enumerate(items):
            ax.text(x, 3.2 - i*0.6, f'• {item}', fontsize=8, ha='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('cloud-scalability-patterns.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated cloud-scalability-patterns.svg")
    plt.close(fig)
