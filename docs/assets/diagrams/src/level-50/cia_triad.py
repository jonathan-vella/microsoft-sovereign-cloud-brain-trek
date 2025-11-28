#!/usr/bin/env python3
"""
CIA Triad Security Diagram
Replaces Mermaid diagram in security-compliance-basics.md
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

# CIA colors
CONF_COLOR = '#1565C0'  # Blue for Confidentiality
INT_COLOR = '#2E7D32'   # Green for Integrity
AVAIL_COLOR = '#E65100'  # Orange for Availability


def create_cia_triad():
    """Create a CIA Triad diagram with subcategories."""

    fig, ax = plt.subplots(figsize=(12, 10))

    # Triangle center and size
    center_x, center_y = 0.5, 0.45
    size = 0.25

    # Triangle vertices (equilateral)
    angles = [90, 210, 330]  # Top, bottom-left, bottom-right
    vertices = []
    for angle in angles:
        rad = np.radians(angle)
        x = center_x + size * np.cos(rad)
        y = center_y + size * np.sin(rad)
        vertices.append((x, y))

    # Draw connecting lines between vertices
    for i in range(3):
        j = (i + 1) % 3
        ax.plot([vertices[i][0], vertices[j][0]],
                [vertices[i][1], vertices[j][1]],
                color='#666666', linewidth=2, zorder=1)

    # CIA properties
    cia = [
        {
            'name': 'Confidentiality',
            'icon': '🔒',
            'color': CONF_COLOR,
            'vertex': vertices[0],
            'items': ['Access Controls', 'Encryption', 'Authentication'],
            'item_dir': 'up'
        },
        {
            'name': 'Integrity',
            'icon': '✅',
            'color': INT_COLOR,
            'vertex': vertices[1],
            'items': ['Checksums', 'Digital Signatures', 'Version Control'],
            'item_dir': 'left'
        },
        {
            'name': 'Availability',
            'icon': '⚡',
            'color': AVAIL_COLOR,
            'vertex': vertices[2],
            'items': ['Redundancy', 'Backups', 'Disaster Recovery'],
            'item_dir': 'right'
        },
    ]

    for prop in cia:
        x, y = prop['vertex']

        # Main node
        circle = plt.Circle((x, y), 0.08, facecolor=prop['color'],
                            edgecolor='white', linewidth=3, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y + 0.01, prop['icon'], ha='center', va='center',
                fontsize=16, zorder=6)
        ax.text(x, y - 0.04, prop['name'], ha='center', va='center',
                fontsize=9, fontweight='bold', color='white', zorder=6)

        # Sub-items
        if prop['item_dir'] == 'up':
            for i, item in enumerate(prop['items']):
                ix = x - 0.15 + i * 0.15
                iy = y + 0.18 + (1 - abs(i - 1)) * 0.05

                ax.plot([x, ix], [y + 0.08, iy - 0.025],
                        color=prop['color'], linewidth=1.5, alpha=0.6)

                box = mpatches.FancyBboxPatch(
                    (ix - 0.065, iy - 0.025), 0.13, 0.05,
                    boxstyle="round,pad=0.01", facecolor=prop['color'],
                    edgecolor='white', linewidth=1, alpha=0.8
                )
                ax.add_patch(box)
                ax.text(ix, iy, item, ha='center', va='center',
                        fontsize=7, color='white')

        elif prop['item_dir'] == 'left':
            for i, item in enumerate(prop['items']):
                ix = x - 0.2
                iy = y + 0.08 - i * 0.07

                ax.plot([x - 0.08, ix + 0.065], [y, iy],
                        color=prop['color'], linewidth=1.5, alpha=0.6)

                box = mpatches.FancyBboxPatch(
                    (ix - 0.08, iy - 0.02), 0.14, 0.04,
                    boxstyle="round,pad=0.01", facecolor=prop['color'],
                    edgecolor='white', linewidth=1, alpha=0.8
                )
                ax.add_patch(box)
                ax.text(ix - 0.01, iy, item, ha='center', va='center',
                        fontsize=7, color='white')

        else:  # right
            for i, item in enumerate(prop['items']):
                ix = x + 0.2
                iy = y + 0.08 - i * 0.07

                ax.plot([x + 0.08, ix - 0.065], [y, iy],
                        color=prop['color'], linewidth=1.5, alpha=0.6)

                box = mpatches.FancyBboxPatch(
                    (ix - 0.06, iy - 0.02), 0.14, 0.04,
                    boxstyle="round,pad=0.01", facecolor=prop['color'],
                    edgecolor='white', linewidth=1, alpha=0.8
                )
                ax.add_patch(box)
                ax.text(ix + 0.01, iy, item, ha='center', va='center',
                        fontsize=7, color='white')

    # Center label
    ax.text(center_x, center_y - 0.05, 'CIA\nTriad', ha='center', va='center',
            fontsize=11, fontweight='bold', color=AZURE_DARK_BLUE)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0.5, 0.95, '🔐 The CIA Triad - Foundation of Information Security',
            ha='center', va='top', fontsize=14, fontweight='bold',
            color=AZURE_DARK_BLUE)

    plt.tight_layout()
    return fig


def main():
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-50'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating CIA Triad Diagram...")
    fig = create_cia_triad()

    output_path = output_dir / 'cia-triad.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)


if __name__ == '__main__':
    main()
