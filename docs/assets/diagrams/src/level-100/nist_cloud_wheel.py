#!/usr/bin/env python3
"""
NIST Cloud Characteristics Wheel
Illustrates the 5 essential characteristics of cloud computing per NIST SP 800-145.
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
AZURE_PURPLE = '#5C2D91'
AZURE_RED = '#D13438'


def create_nist_wheel():
    """Create a wheel diagram of NIST cloud characteristics."""

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

    # 5 NIST essential characteristics
    characteristics = [
        'On-Demand\nSelf-Service',
        'Broad\nNetwork Access',
        'Resource\nPooling',
        'Rapid\nElasticity',
        'Measured\nService'
    ]

    # Descriptions for each
    descriptions = [
        'Provision computing\ncapabilities as needed\nautomatically',
        'Capabilities available\nover the network via\nstandard mechanisms',
        'Provider resources pooled\nto serve multiple consumers\ndynamically',
        'Capabilities can be\nprovisioned/released\nelastically',
        'Resource usage\nmonitored, controlled,\nand reported'
    ]

    colors = [AZURE_BLUE, AZURE_GREEN, AZURE_PURPLE, AZURE_ORANGE, AZURE_RED]

    n = len(characteristics)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()

    # Close the polygon
    angles += angles[:1]

    # Create outer ring for characteristic names
    for i, (char, desc, color, angle) in enumerate(zip(characteristics, descriptions, colors, angles[:-1])):
        # Outer segment
        theta1 = angle - np.pi / n
        theta2 = angle + np.pi / n

        # Draw wedge
        wedge = mpatches.Wedge((0, 0), 1.0, np.degrees(theta1) - 90, np.degrees(theta2) - 90,
                                width=0.35, facecolor=color, edgecolor='white',
                                linewidth=2, alpha=0.9,
                                transform=ax.transData + ax.transAxes)

        # Position for text
        text_angle = angle
        text_radius = 0.85

        # Rotate text for readability
        rotation = np.degrees(text_angle) - 90
        if 90 < np.degrees(text_angle) < 270:
            rotation += 180

        # Add characteristic name
        ax.text(text_angle, text_radius, char, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white',
                rotation=rotation if abs(rotation) < 90 else rotation - 180)

    # Create wedges manually since polar doesn't support them well
    ax.set_ylim(0, 1.2)

    # Draw the wheel using filled areas
    for i, (color, angle) in enumerate(zip(colors, angles[:-1])):
        theta1 = angle - np.pi / n + 0.02
        theta2 = angle + np.pi / n - 0.02
        theta = np.linspace(theta1, theta2, 50)

        # Outer arc
        r_outer = np.ones(50)
        r_inner = np.ones(50) * 0.65

        ax.fill_between(theta, r_inner, r_outer, color=color, alpha=0.9)

        # Add characteristic text
        text_angle = angle
        ax.text(text_angle, 0.825, characteristics[i], ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')

    # Center circle
    center_circle = plt.Circle((0, 0), 0.5, transform=ax.transData + ax.transAxes,
                                facecolor='white', edgecolor=AZURE_DARK_BLUE, linewidth=3)

    # Add descriptions in center area
    for i, (desc, color, angle) in enumerate(zip(descriptions, colors, angles[:-1])):
        text_angle = angle
        ax.text(text_angle, 0.35, desc, ha='center', va='center',
                fontsize=7, color=color, alpha=0.9)

    # Inner ring with descriptions
    for i, (desc, color, angle) in enumerate(zip(descriptions, colors, angles[:-1])):
        theta1 = angle - np.pi / n + 0.02
        theta2 = angle + np.pi / n - 0.02
        theta = np.linspace(theta1, theta2, 50)

        r_outer = np.ones(50) * 0.63
        r_inner = np.ones(50) * 0.25

        ax.fill_between(theta, r_inner, r_outer, color=color, alpha=0.2)

        # Add description text
        ax.text(angle, 0.44, desc, ha='center', va='center',
                fontsize=7, color=color, fontweight='500')

    # Center label
    center = plt.Circle((0, 0), 0.23, transform=ax.transData + ax.transAxes,
                         facecolor=AZURE_DARK_BLUE, edgecolor='white', linewidth=2)
    ax.text(0, 0, 'NIST\nCloud\nModel', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Remove polar elements
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.spines['polar'].set_visible(False)
    ax.grid(False)

    # Title
    ax.set_title('NIST Essential Cloud Characteristics\n(SP 800-145)',
                 fontsize=14, fontweight='bold', color=AZURE_DARK_BLUE, pad=20)

    return fig


def main():
    """Generate and save the NIST wheel."""

    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating NIST Cloud Characteristics Wheel...")

    fig = create_nist_wheel()

    output_path = output_dir / 'nist-cloud-characteristics.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)
    print("✅ Wheel generated successfully!")


if __name__ == '__main__':
    main()
