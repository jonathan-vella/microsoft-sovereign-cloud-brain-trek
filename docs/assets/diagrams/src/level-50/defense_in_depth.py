#!/usr/bin/env python3
"""
Defense in Depth Security Layers Diagram
Replaces Mermaid diagram in security-compliance-basics.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Layer colors (rainbow gradient)
LAYER_COLORS = [
    '#C62828',  # Physical - Red
    '#EF6C00',  # Network - Orange
    '#F9A825',  # Endpoint - Yellow
    '#2E7D32',  # Application - Green
    '#1565C0',  # Data - Blue
    '#6A1B9A',  # Identity - Purple
    '#37474F',  # Administrative - Grey
]

AZURE_DARK_BLUE = '#004578'


def create_defense_in_depth():
    """Create a Defense in Depth layers diagram."""

    fig, ax = plt.subplots(figsize=(14, 10))

    layers = [
        ('🏢 Physical Security', 'Data centers, locks, biometrics, guards'),
        ('🌐 Network Security', 'Firewalls, VPNs, segmentation, DDoS protection'),
        ('💻 Endpoint Security', 'Antivirus, patching, device encryption'),
        ('📱 Application Security', 'WAF, input validation, SAST/DAST'),
        ('💾 Data Security', 'Encryption, DLP, classification, masking'),
        ('👤 Identity Security', 'MFA, RBAC, SSO, privileged access'),
        ('📋 Administrative Controls', 'Policies, training, audits, governance'),
    ]

    # Draw concentric arcs (half circles) representing layers
    center_x, center_y = 0.5, 0.15
    base_radius = 0.15
    layer_thickness = 0.1

    for i, ((name, desc), color) in enumerate(zip(layers, LAYER_COLORS)):
        inner_r = base_radius + i * layer_thickness
        outer_r = inner_r + layer_thickness - 0.01

        # Draw arc
        theta = np.linspace(0, np.pi, 100)
        inner_x = center_x + inner_r * np.cos(theta)
        inner_y = center_y + inner_r * np.sin(theta)
        outer_x = center_x + outer_r * np.cos(theta[::-1])
        outer_y = center_y + outer_r * np.sin(theta[::-1])

        x = np.concatenate([inner_x, outer_x])
        y = np.concatenate([inner_y, outer_y])

        ax.fill(x, y, facecolor=color, edgecolor='white', linewidth=2, alpha=0.85)

        # Layer label on the arc
        mid_r = (inner_r + outer_r) / 2
        label_y = center_y + mid_r * 0.85
        ax.text(center_x, label_y, name, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

        # Description on the right
        desc_x = center_x + outer_r + 0.08
        desc_y = center_y + mid_r * 0.7

        # Connecting line
        ax.plot([center_x + outer_r * 0.95, desc_x - 0.02],
                [center_y + mid_r * 0.7, desc_y],
                color=color, linewidth=1.5, linestyle='--', alpha=0.7)

        ax.text(desc_x, desc_y, desc, ha='left', va='center',
                fontsize=8, color=color, style='italic')

    # Asset at center
    asset = plt.Circle((center_x, center_y + 0.08), 0.06,
                        facecolor='#FFD700', edgecolor='white', linewidth=2)
    ax.add_patch(asset)
    ax.text(center_x, center_y + 0.08, '🎯\nAsset', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#333333')

    # Attacker arrow
    ax.annotate('', xy=(center_x, center_y + 0.9),
                xytext=(center_x, center_y + 1.0),
                arrowprops=dict(arrowstyle='->', color='#D32F2F', lw=3))
    ax.text(center_x, center_y + 1.02, '🎯 Attacker', ha='center', va='bottom',
            fontsize=10, color='#D32F2F', fontweight='bold')

    # Legend
    ax.text(0.05, 0.95, 'Defense in Depth: Multiple security layers protect assets',
            ha='left', va='top', fontsize=10, color='#666666', style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(0.5, 1.08, '🛡️ Defense in Depth - Layered Security Model',
            ha='center', va='top', fontsize=14, fontweight='bold',
            color=AZURE_DARK_BLUE)

    plt.tight_layout()
    return fig


# Need numpy for the arcs
import numpy as np


def main():
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-50'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Defense in Depth Diagram...")
    fig = create_defense_in_depth()

    output_path = output_dir / 'defense-in-depth.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)


if __name__ == '__main__':
    main()
