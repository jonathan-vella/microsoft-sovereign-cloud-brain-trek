#!/usr/bin/env python3
"""
Hypervisor Types Comparison Diagram
Replaces Mermaid diagram in cloud-computing-primer.md
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_GREEN = '#107C10'
AZURE_LIGHT_GREEN = '#D4E9D7'
AZURE_ORANGE = '#FF8C00'
AZURE_LIGHT_ORANGE = '#FFF4E6'


def create_hypervisor_types():
    """Create a comparison of Type 1 and Type 2 hypervisors."""

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

    # Type 1 Hypervisor (Bare Metal)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')

    # Background
    bg1 = mpatches.FancyBboxPatch(
        (0.05, 0.05), 0.9, 0.85, boxstyle="round,pad=0.02",
        facecolor=AZURE_LIGHT_GREEN, edgecolor=AZURE_GREEN,
        linewidth=3, alpha=0.5
    )
    ax1.add_patch(bg1)

    # Title
    ax1.text(0.5, 0.95, 'Type 1: Bare Metal Hypervisor', ha='center', va='top',
             fontsize=12, fontweight='bold', color=AZURE_GREEN)

    # Hardware layer
    hw1 = mpatches.FancyBboxPatch(
        (0.1, 0.1), 0.8, 0.12, boxstyle="round,pad=0.01",
        facecolor='#666666', edgecolor='white', linewidth=2
    )
    ax1.add_patch(hw1)
    ax1.text(0.5, 0.16, 'Physical Hardware\n(CPU, RAM, Storage, Network)',
             ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # Hypervisor layer
    hv1 = mpatches.FancyBboxPatch(
        (0.1, 0.25), 0.8, 0.12, boxstyle="round,pad=0.01",
        facecolor=AZURE_GREEN, edgecolor='white', linewidth=2
    )
    ax1.add_patch(hv1)
    ax1.text(0.5, 0.31, 'Hypervisor (Hyper-V, ESXi, KVM)',
             ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    # VMs
    vm_colors = [AZURE_BLUE, AZURE_ORANGE, AZURE_DARK_BLUE]
    vm_labels = ['VM 1\nWindows', 'VM 2\nLinux', 'VM 3\nWindows']
    for i, (color, label) in enumerate(zip(vm_colors, vm_labels)):
        x = 0.15 + i * 0.28
        vm = mpatches.FancyBboxPatch(
            (x, 0.45), 0.22, 0.35, boxstyle="round,pad=0.01",
            facecolor=color, edgecolor='white', linewidth=2
        )
        ax1.add_patch(vm)
        ax1.text(x + 0.11, 0.625, label, ha='center', va='center',
                 fontsize=9, color='white', fontweight='bold')

    # Arrows from hypervisor to VMs
    for i in range(3):
        x = 0.26 + i * 0.28
        ax1.annotate('', xy=(x, 0.45), xytext=(x, 0.37),
                     arrowprops=dict(arrowstyle='->', color=AZURE_GREEN, lw=2))

    # Benefits
    ax1.text(0.5, 0.88, '✓ Better Performance  ✓ Direct Hardware Access  ✓ Enterprise Grade',
             ha='center', va='center', fontsize=8, color=AZURE_GREEN)

    # Type 2 Hypervisor (Hosted)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    # Background
    bg2 = mpatches.FancyBboxPatch(
        (0.05, 0.05), 0.9, 0.85, boxstyle="round,pad=0.02",
        facecolor=AZURE_LIGHT_ORANGE, edgecolor=AZURE_ORANGE,
        linewidth=3, alpha=0.5
    )
    ax2.add_patch(bg2)

    # Title
    ax2.text(0.5, 0.95, 'Type 2: Hosted Hypervisor', ha='center', va='top',
             fontsize=12, fontweight='bold', color=AZURE_ORANGE)

    # Hardware layer
    hw2 = mpatches.FancyBboxPatch(
        (0.1, 0.1), 0.8, 0.1, boxstyle="round,pad=0.01",
        facecolor='#666666', edgecolor='white', linewidth=2
    )
    ax2.add_patch(hw2)
    ax2.text(0.5, 0.15, 'Physical Hardware',
             ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # Host OS layer
    os2 = mpatches.FancyBboxPatch(
        (0.1, 0.22), 0.8, 0.1, boxstyle="round,pad=0.01",
        facecolor='#5C2D91', edgecolor='white', linewidth=2
    )
    ax2.add_patch(os2)
    ax2.text(0.5, 0.27, 'Host Operating System (Windows, macOS, Linux)',
             ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # Hypervisor layer
    hv2 = mpatches.FancyBboxPatch(
        (0.1, 0.34), 0.8, 0.1, boxstyle="round,pad=0.01",
        facecolor=AZURE_ORANGE, edgecolor='white', linewidth=2
    )
    ax2.add_patch(hv2)
    ax2.text(0.5, 0.39, 'Hypervisor (VirtualBox, VMware Workstation)',
             ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    # VMs
    vm_colors2 = [AZURE_BLUE, AZURE_DARK_BLUE]
    vm_labels2 = ['VM 1', 'VM 2']
    for i, (color, label) in enumerate(zip(vm_colors2, vm_labels2)):
        x = 0.2 + i * 0.35
        vm = mpatches.FancyBboxPatch(
            (x, 0.5), 0.25, 0.28, boxstyle="round,pad=0.01",
            facecolor=color, edgecolor='white', linewidth=2
        )
        ax2.add_patch(vm)
        ax2.text(x + 0.125, 0.64, label, ha='center', va='center',
                 fontsize=10, color='white', fontweight='bold')

    # Arrows
    for i in range(2):
        x = 0.325 + i * 0.35
        ax2.annotate('', xy=(x, 0.5), xytext=(x, 0.44),
                     arrowprops=dict(arrowstyle='->', color=AZURE_ORANGE, lw=2))

    # Benefits
    ax2.text(0.5, 0.88, '✓ Easy Setup  ✓ Development/Testing  ✓ Desktop Use',
             ha='center', va='center', fontsize=8, color=AZURE_ORANGE)

    plt.suptitle('Hypervisor Types Comparison', fontsize=16, fontweight='bold',
                 color=AZURE_DARK_BLUE, y=1.02)

    plt.tight_layout()
    return fig


def main():
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-50'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Hypervisor Types Diagram...")
    fig = create_hypervisor_types()

    output_path = output_dir / 'hypervisor-types.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)


if __name__ == '__main__':
    main()
