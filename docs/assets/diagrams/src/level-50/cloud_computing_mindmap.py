#!/usr/bin/env python3
"""
Cloud Computing Mindmap - NIST 5 Essential Characteristics
Replaces Mermaid mindmap in cloud-computing-primer.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_GREEN = '#107C10'
AZURE_LIGHT_BLUE = '#E8F4FD'
AZURE_ORANGE = '#FF8C00'
AZURE_PURPLE = '#5C2D91'
AZURE_RED = '#D13438'


def create_cloud_mindmap():
    """Create a mindmap of cloud computing characteristics."""

    fig, ax = plt.subplots(figsize=(14, 10))

    # Center circle - Cloud Computing
    center = plt.Circle((0.5, 0.5), 0.12, facecolor=AZURE_BLUE,
                         edgecolor='white', linewidth=3, zorder=10)
    ax.add_patch(center)
    ax.text(0.5, 0.5, 'Cloud\nComputing', ha='center', va='center',
            fontsize=14, fontweight='bold', color='white', zorder=11)

    # Five characteristics with their sub-items
    characteristics = [
        {
            'name': 'On-Demand\nSelf-Service',
            'color': AZURE_GREEN,
            'angle': 90,
            'items': ['Automatic provisioning', 'No human interaction', 'Instant access']
        },
        {
            'name': 'Broad\nNetwork Access',
            'color': AZURE_PURPLE,
            'angle': 162,
            'items': ['Multi-platform support', 'Standard protocols', 'Internet available']
        },
        {
            'name': 'Resource\nPooling',
            'color': AZURE_ORANGE,
            'angle': 234,
            'items': ['Multi-tenant model', 'Dynamic allocation', 'Location independence']
        },
        {
            'name': 'Rapid\nElasticity',
            'color': AZURE_RED,
            'angle': 306,
            'items': ['Scale out/in quickly', 'Appears unlimited', 'Demand-based']
        },
        {
            'name': 'Measured\nService',
            'color': AZURE_DARK_BLUE,
            'angle': 18,
            'items': ['Pay-per-use', 'Monitoring & reporting', 'Transparent billing']
        },
    ]

    center_x, center_y = 0.5, 0.5
    main_radius = 0.28
    sub_radius = 0.42

    for char in characteristics:
        angle_rad = np.radians(char['angle'])

        # Main characteristic node
        x = center_x + main_radius * np.cos(angle_rad)
        y = center_y + main_radius * np.sin(angle_rad)

        # Draw connecting line to center
        ax.plot([center_x, x], [center_y, y], color=char['color'],
                linewidth=3, zorder=1)

        # Main node
        node = plt.Circle((x, y), 0.08, facecolor=char['color'],
                          edgecolor='white', linewidth=2, zorder=5)
        ax.add_patch(node)
        ax.text(x, y, char['name'], ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', zorder=6)

        # Sub-items
        sub_angle_spread = 25
        start_angle = char['angle'] - sub_angle_spread
        angle_step = sub_angle_spread

        for i, item in enumerate(char['items']):
            sub_angle = start_angle + i * angle_step
            sub_angle_rad = np.radians(sub_angle)

            sx = center_x + sub_radius * np.cos(sub_angle_rad)
            sy = center_y + sub_radius * np.sin(sub_angle_rad)

            # Line from main node to sub-item
            ax.plot([x, sx], [y, sy], color=char['color'],
                    linewidth=1.5, alpha=0.6, zorder=1)

            # Sub-item node
            sub_node = mpatches.FancyBboxPatch(
                (sx - 0.07, sy - 0.025), 0.14, 0.05,
                boxstyle="round,pad=0.01", facecolor=char['color'],
                edgecolor='white', linewidth=1, alpha=0.8, zorder=4
            )
            ax.add_patch(sub_node)
            ax.text(sx, sy, item, ha='center', va='center',
                    fontsize=7, color='white', zorder=5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0.5, 0.95, 'NIST Cloud Computing Essential Characteristics',
            ha='center', va='top', fontsize=14, fontweight='bold',
            color=AZURE_DARK_BLUE)

    plt.tight_layout()
    return fig


def main():
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-50'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Cloud Computing Mindmap...")
    fig = create_cloud_mindmap()

    output_path = output_dir / 'cloud-computing-mindmap.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)


if __name__ == '__main__':
    main()
