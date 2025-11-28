#!/usr/bin/env python3
"""
Traditional IT vs Cloud Computing Comparison
Replaces Mermaid flowchart in cloud-computing-primer.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_LIGHT_BLUE = '#E8F4FD'
TRADITIONAL_RED = '#D13438'
TRADITIONAL_LIGHT = '#FFEBEE'


def create_traditional_vs_cloud():
    """Create a comparison diagram of Traditional IT vs Cloud Computing."""

    fig, ax = plt.subplots(figsize=(14, 8))

    # Traditional IT Column
    trad_x = 0.22
    trad_steps = [
        ('Purchase Hardware', '💰 Large CapEx'),
        ('Install & Configure', '📅 Weeks/Months'),
        ('Maintain & Patch', '👨‍💻 IT Staff'),
        ('Scale Manually', '⏰ Lead Time'),
        ('Decommission', '📦 E-waste'),
    ]

    # Cloud Column
    cloud_x = 0.78
    cloud_steps = [
        ('Request Resources', '🖱️ Self-service'),
        ('Instant Provisioning', '⚡ Minutes'),
        ('Managed by Provider', '🔧 PaaS/SaaS'),
        ('Auto-Scale', '📈 Elastic'),
        ('Pay per Use', '💳 OpEx'),
    ]

    # Draw Traditional IT section
    trad_box = mpatches.FancyBboxPatch(
        (0.02, 0.1), 0.4, 0.8, boxstyle="round,pad=0.02",
        facecolor=TRADITIONAL_LIGHT, edgecolor=TRADITIONAL_RED,
        linewidth=3, alpha=0.7
    )
    ax.add_patch(trad_box)
    ax.text(trad_x, 0.92, '🏢 Traditional IT', ha='center', va='center',
            fontsize=14, fontweight='bold', color=TRADITIONAL_RED)

    # Draw Cloud section
    cloud_box = mpatches.FancyBboxPatch(
        (0.58, 0.1), 0.4, 0.8, boxstyle="round,pad=0.02",
        facecolor=AZURE_LIGHT_BLUE, edgecolor=AZURE_BLUE,
        linewidth=3, alpha=0.7
    )
    ax.add_patch(cloud_box)
    ax.text(cloud_x, 0.92, '☁️ Cloud Computing', ha='center', va='center',
            fontsize=14, fontweight='bold', color=AZURE_BLUE)

    # Draw steps
    y_start = 0.78
    y_step = 0.13

    for i, ((trad_title, trad_sub), (cloud_title, cloud_sub)) in enumerate(zip(trad_steps, cloud_steps)):
        y = y_start - i * y_step

        # Traditional step
        trad_node = mpatches.FancyBboxPatch(
            (trad_x - 0.15, y - 0.04), 0.3, 0.08,
            boxstyle="round,pad=0.01", facecolor=TRADITIONAL_RED,
            edgecolor='white', linewidth=2
        )
        ax.add_patch(trad_node)
        ax.text(trad_x, y, trad_title, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')
        ax.text(trad_x, y - 0.06, trad_sub, ha='center', va='center',
                fontsize=7, color='#666666', style='italic')

        # Cloud step
        cloud_node = mpatches.FancyBboxPatch(
            (cloud_x - 0.15, y - 0.04), 0.3, 0.08,
            boxstyle="round,pad=0.01", facecolor=AZURE_BLUE,
            edgecolor='white', linewidth=2
        )
        ax.add_patch(cloud_node)
        ax.text(cloud_x, y, cloud_title, ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')
        ax.text(cloud_x, y + 0.06, cloud_sub, ha='center', va='center',
                fontsize=7, color='#666666', style='italic')

        # Arrow down (except last)
        if i < len(trad_steps) - 1:
            ax.annotate('', xy=(trad_x, y - 0.08), xytext=(trad_x, y - 0.05),
                        arrowprops=dict(arrowstyle='->', color=TRADITIONAL_RED, lw=2))
            ax.annotate('', xy=(cloud_x, y - 0.08), xytext=(cloud_x, y - 0.05),
                        arrowprops=dict(arrowstyle='->', color=AZURE_BLUE, lw=2))

    # Center comparison arrow
    ax.annotate('', xy=(0.55, 0.5), xytext=(0.45, 0.5),
                arrowprops=dict(arrowstyle='<->', color='#666666', lw=2))

    # Time comparison
    ax.text(0.5, 0.55, 'Weeks/Months', ha='center', va='center',
            fontsize=8, color=TRADITIONAL_RED, fontweight='bold')
    ax.text(0.5, 0.45, 'vs Minutes', ha='center', va='center',
            fontsize=8, color=AZURE_BLUE, fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0.5, 0.98, 'Traditional IT vs Cloud Computing',
            ha='center', va='top', fontsize=16, fontweight='bold',
            color=AZURE_DARK_BLUE)

    plt.tight_layout()
    return fig


def main():
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-50'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Traditional vs Cloud Comparison...")
    fig = create_traditional_vs_cloud()

    output_path = output_dir / 'traditional-vs-cloud.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)


if __name__ == '__main__':
    main()
