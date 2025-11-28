#!/usr/bin/env python3
"""
Data Classification Pyramid
Shows the hierarchy of data classification levels for sovereignty.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_RED = '#D13438'
AZURE_PURPLE = '#5C2D91'


def create_data_classification_pyramid():
    """Create a pyramid diagram for data classification levels."""

    fig, ax = plt.subplots(figsize=(12, 10))

    # Classification levels (bottom to top)
    levels = [
        {
            'name': 'PUBLIC',
            'color': AZURE_GREEN,
            'description': 'Freely available information',
            'examples': 'Press releases, marketing materials, public documentation',
            'controls': 'No special controls required'
        },
        {
            'name': 'INTERNAL',
            'color': AZURE_BLUE,
            'description': 'Business operational data',
            'examples': 'Internal policies, procedures, org charts',
            'controls': 'Access limited to employees'
        },
        {
            'name': 'CONFIDENTIAL',
            'color': AZURE_ORANGE,
            'description': 'Sensitive business information',
            'examples': 'Financial data, customer PII, contracts',
            'controls': 'Encryption, access logging, need-to-know'
        },
        {
            'name': 'RESTRICTED',
            'color': AZURE_RED,
            'description': 'Highly sensitive / regulated data',
            'examples': 'Health records (PHI), payment data (PCI), classified',
            'controls': 'Strong encryption, strict access, air-gapped options'
        },
        {
            'name': 'TOP SECRET',
            'color': AZURE_PURPLE,
            'description': 'National security / critical infrastructure',
            'examples': 'Defense systems, intelligence data, ITAR',
            'controls': 'Air-gapped, sovereign cloud, hardware security'
        }
    ]

    n = len(levels)
    pyramid_height = 8
    base_width = 10

    # Draw pyramid layers from bottom to top
    for i, level in enumerate(levels):
        # Calculate layer dimensions
        y_bottom = i * pyramid_height / n
        y_top = (i + 1) * pyramid_height / n

        width_bottom = base_width * (1 - i / n)
        width_top = base_width * (1 - (i + 1) / n)

        # Create trapezoid vertices
        vertices = [
            (-width_bottom / 2, y_bottom),
            (width_bottom / 2, y_bottom),
            (width_top / 2, y_top),
            (-width_top / 2, y_top)
        ]

        # Draw layer
        polygon = mpatches.Polygon(vertices, facecolor=level['color'],
                                    edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(polygon)

        # Add level name
        y_center = (y_bottom + y_top) / 2
        ax.text(0, y_center, level['name'], ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

        # Add description to the right
        x_right = base_width / 2 + 0.5
        ax.text(x_right, y_center + 0.15, level['description'], ha='left', va='center',
                fontsize=10, fontweight='bold', color=level['color'])
        ax.text(x_right, y_center - 0.15, level['examples'], ha='left', va='center',
                fontsize=8, color='#666666', style='italic')

        # Add controls to the left
        x_left = -base_width / 2 - 0.5
        ax.text(x_left, y_center, level['controls'], ha='right', va='center',
                fontsize=9, color=level['color'])

        # Add connecting line
        ax.plot([width_bottom / 2, x_right - 0.1], [y_center, y_center],
                color=level['color'], linewidth=1, linestyle='--', alpha=0.5)

    # Labels
    ax.text(0, pyramid_height + 0.8, 'Data Classification Pyramid',
            ha='center', va='center', fontsize=16, fontweight='bold',
            color=AZURE_DARK_BLUE)
    ax.text(0, pyramid_height + 0.3, 'Higher levels require stronger sovereignty controls',
            ha='center', va='center', fontsize=11, color='#666666', style='italic')

    # Side labels
    ax.text(base_width / 2 + 3, pyramid_height / 2, 'CLASSIFICATION & EXAMPLES',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=AZURE_DARK_BLUE, rotation=90)
    ax.text(-base_width / 2 - 3, pyramid_height / 2, 'SECURITY CONTROLS',
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=AZURE_DARK_BLUE, rotation=90)

    # Sensitivity arrow
    ax.annotate('', xy=(-base_width / 2 - 1.5, pyramid_height - 0.5),
                xytext=(-base_width / 2 - 1.5, 0.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK_BLUE, lw=2))
    ax.text(-base_width / 2 - 1.8, pyramid_height / 2, 'SENSITIVITY',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=AZURE_DARK_BLUE, rotation=90)

    # Volume arrow
    ax.annotate('', xy=(base_width / 2 + 5.5, 0.5),
                xytext=(base_width / 2 + 5.5, pyramid_height - 0.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK_BLUE, lw=2))
    ax.text(base_width / 2 + 5.8, pyramid_height / 2, 'DATA VOLUME',
            ha='center', va='center', fontsize=9, fontweight='bold',
            color=AZURE_DARK_BLUE, rotation=90)

    # Set limits and remove axes
    ax.set_xlim(-8, 12)
    ax.set_ylim(-0.5, pyramid_height + 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    return fig


def main():
    """Generate and save the data classification pyramid."""

    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Data Classification Pyramid...")

    fig = create_data_classification_pyramid()

    output_path = output_dir / 'data-classification-pyramid.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)
    print("✅ Pyramid generated successfully!")


if __name__ == '__main__':
    main()
