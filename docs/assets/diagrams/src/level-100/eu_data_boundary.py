#!/usr/bin/env python3
"""
EU Data Boundary Diagram
Shows the Microsoft EU Data Boundary concept and data flow controls.
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


def create_eu_data_boundary():
    """Create a diagram showing the EU Data Boundary concept."""

    fig, ax = plt.subplots(figsize=(14, 10))

    # EU Boundary zone (main area)
    eu_boundary = mpatches.FancyBboxPatch(
        (1, 1), 12, 7, boxstyle="round,pad=0.3",
        facecolor=AZURE_PURPLE, edgecolor=AZURE_PURPLE,
        linewidth=3, alpha=0.15
    )
    ax.add_patch(eu_boundary)

    # EU Boundary border (dashed)
    eu_border = mpatches.FancyBboxPatch(
        (1, 1), 12, 7, boxstyle="round,pad=0.3",
        facecolor='none', edgecolor=AZURE_PURPLE,
        linewidth=3, linestyle='--', alpha=0.8
    )
    ax.add_patch(eu_border)

    # EU Label
    ax.text(7, 7.7, 'EU DATA BOUNDARY', ha='center', va='center',
            fontsize=14, fontweight='bold', color=AZURE_PURPLE)
    ax.text(7, 7.3, 'Microsoft commitment: Customer data stays in EU',
            ha='center', va='center', fontsize=10, color='#666666', style='italic')

    # Azure regions within EU
    regions = [
        {'name': 'West Europe\n(Netherlands)', 'x': 3, 'y': 5.5, 'color': AZURE_BLUE},
        {'name': 'North Europe\n(Ireland)', 'x': 3, 'y': 3.5, 'color': AZURE_BLUE},
        {'name': 'France Central\n(Paris)', 'x': 5.5, 'y': 5.5, 'color': AZURE_BLUE},
        {'name': 'Germany West\n(Frankfurt)', 'x': 5.5, 'y': 3.5, 'color': AZURE_BLUE},
        {'name': 'Sweden Central\n(Stockholm)', 'x': 8, 'y': 5.5, 'color': AZURE_BLUE},
        {'name': 'Switzerland\n(Zürich)', 'x': 8, 'y': 3.5, 'color': AZURE_GREEN},
        {'name': 'Italy North\n(Milan)', 'x': 10.5, 'y': 5.5, 'color': AZURE_BLUE},
        {'name': 'Poland Central\n(Warsaw)', 'x': 10.5, 'y': 3.5, 'color': AZURE_BLUE},
    ]

    for region in regions:
        # Region box
        rect = mpatches.FancyBboxPatch(
            (region['x'] - 1, region['y'] - 0.6), 2, 1.2,
            boxstyle="round,pad=0.1", facecolor=region['color'],
            edgecolor='white', linewidth=2, alpha=0.9
        )
        ax.add_patch(rect)
        ax.text(region['x'], region['y'], region['name'], ha='center', va='center',
                fontsize=8, fontweight='bold', color='white')

    # Data types staying in EU
    ax.text(2.5, 2, 'Data Types Within Boundary:', ha='left', va='center',
            fontsize=10, fontweight='bold', color=AZURE_DARK_BLUE)

    data_types = [
        '✓ Customer Data (content you create)',
        '✓ Personal Data (employee/user info)',
        '✓ Diagnostic Data (system telemetry)',
        '✓ Service-Generated Data'
    ]

    for i, dtype in enumerate(data_types):
        ax.text(2.5, 1.6 - i * 0.35, dtype, ha='left', va='center',
                fontsize=9, color=AZURE_GREEN)

    # External connections (outside boundary)
    # Global Services (outside EU)
    global_box = mpatches.FancyBboxPatch(
        (14, 4), 3, 2, boxstyle="round,pad=0.2",
        facecolor=AZURE_ORANGE, edgecolor='white', linewidth=2, alpha=0.9
    )
    ax.add_patch(global_box)
    ax.text(15.5, 5.3, 'Global Services', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(15.5, 4.8, '(Limited Data)', ha='center', va='center',
            fontsize=8, color='white', alpha=0.8)
    ax.text(15.5, 4.3, '• Authentication\n• Directory sync\n• Security signals',
            ha='center', va='center', fontsize=7, color='white')

    # Connection arrow
    ax.annotate('', xy=(14, 5), xytext=(13.2, 5),
                arrowprops=dict(arrowstyle='->', color=AZURE_ORANGE, lw=2))
    ax.text(13.6, 5.4, 'Minimal\nexposure', ha='center', va='center',
            fontsize=7, color=AZURE_ORANGE)

    # Customer environment (outside EU, left)
    customer_box = mpatches.FancyBboxPatch(
        (-3, 3), 3.5, 3, boxstyle="round,pad=0.2",
        facecolor='#666666', edgecolor='white', linewidth=2, alpha=0.9
    )
    ax.add_patch(customer_box)
    ax.text(-1.25, 5.5, 'Customer\nEnvironment', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(-1.25, 4.3, '• On-premises\n• Branch offices\n• Global operations',
            ha='center', va='center', fontsize=8, color='white')

    # Connection to EU
    ax.annotate('', xy=(0.8, 4.5), xytext=(0.3, 4.5),
                arrowprops=dict(arrowstyle='->', color=AZURE_BLUE, lw=2))
    ax.text(0.55, 5, 'Data stored\nin EU', ha='center', va='center',
            fontsize=7, color=AZURE_BLUE)

    # Key commitments box at bottom
    commitments_box = mpatches.FancyBboxPatch(
        (1, -1.5), 12, 2, boxstyle="round,pad=0.2",
        facecolor='#F5F5F5', edgecolor=AZURE_DARK_BLUE, linewidth=2, alpha=0.95
    )
    ax.add_patch(commitments_box)

    ax.text(7, -0.2, 'EU Data Boundary Commitments', ha='center', va='center',
            fontsize=11, fontweight='bold', color=AZURE_DARK_BLUE)

    commitments = [
        '• Store and process customer data within EU',
        '• Limit transfers to essential global operations',
        '• Encryption with customer-managed keys',
        '• EU-based support with controlled access'
    ]

    for i, commitment in enumerate(commitments):
        col = i % 2
        row = i // 2
        ax.text(2 + col * 6, -0.7 - row * 0.4, commitment, ha='left', va='center',
                fontsize=9, color='#333333')

    # Title
    ax.text(7, 9, 'Microsoft EU Data Boundary',
            ha='center', va='center', fontsize=16, fontweight='bold',
            color=AZURE_DARK_BLUE)
    ax.text(7, 8.5, 'Ensuring European data stays in Europe',
            ha='center', va='center', fontsize=11, color='#666666', style='italic')

    # Set limits
    ax.set_xlim(-4, 18)
    ax.set_ylim(-2, 9.5)
    ax.set_aspect('equal')
    ax.axis('off')

    return fig


def main():
    """Generate and save the EU Data Boundary diagram."""

    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating EU Data Boundary Diagram...")

    fig = create_eu_data_boundary()

    output_path = output_dir / 'eu-data-boundary.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)
    print("✅ Diagram generated successfully!")


if __name__ == '__main__':
    main()
