#!/usr/bin/env python3
"""
CapEx vs OpEx Comparison Chart
Illustrates the cost model differences between traditional IT and cloud.
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


def create_capex_opex_chart():
    """Create a comparison chart of CapEx vs OpEx spending patterns."""

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Time periods (quarters over 3 years)
    quarters = np.arange(12)
    quarter_labels = [f'Q{(i % 4) + 1}' for i in range(12)]

    # CapEx model - large upfront costs, then maintenance
    capex_hardware = np.array([100, 5, 5, 5, 5, 5, 5, 5, 80, 5, 5, 5])
    capex_software = np.array([30, 2, 2, 2, 2, 2, 2, 2, 25, 2, 2, 2])
    capex_staff = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

    # OpEx model - consistent monthly costs
    opex_compute = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    opex_storage = np.array([3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5])
    opex_services = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

    # Left plot - CapEx (Traditional IT)
    ax1.bar(quarters, capex_hardware, label='Hardware', color=AZURE_DARK_BLUE, alpha=0.9)
    ax1.bar(quarters, capex_software, bottom=capex_hardware, label='Software Licenses',
            color=AZURE_BLUE, alpha=0.9)
    ax1.bar(quarters, capex_staff, bottom=capex_hardware + capex_software,
            label='IT Staff', color='#666666', alpha=0.9)

    ax1.set_xlabel('Time (Quarters)', fontsize=11)
    ax1.set_ylabel('Cost (Relative Units)', fontsize=11)
    ax1.set_title('CapEx Model (Traditional IT)', fontsize=13, fontweight='bold',
                  color=AZURE_DARK_BLUE, pad=15)
    ax1.set_xticks(quarters)
    ax1.set_xticklabels(quarter_labels)
    ax1.legend(loc='upper right', fontsize=9)
    ax1.set_ylim(0, 160)

    # Add annotations
    ax1.annotate('Hardware\nRefresh', xy=(0, 140), ha='center', fontsize=9, color=AZURE_DARK_BLUE)
    ax1.annotate('Hardware\nRefresh', xy=(8, 115), ha='center', fontsize=9, color=AZURE_DARK_BLUE)

    # Right plot - OpEx (Cloud)
    ax2.bar(quarters, opex_compute, label='Compute', color=AZURE_GREEN, alpha=0.9)
    ax2.bar(quarters, opex_storage, bottom=opex_compute, label='Storage',
            color=AZURE_BLUE, alpha=0.9)
    ax2.bar(quarters, opex_services, bottom=opex_compute + opex_storage,
            label='Managed Services', color=AZURE_ORANGE, alpha=0.9)

    ax2.set_xlabel('Time (Quarters)', fontsize=11)
    ax2.set_ylabel('Cost (Relative Units)', fontsize=11)
    ax2.set_title('OpEx Model (Cloud)', fontsize=13, fontweight='bold',
                  color=AZURE_GREEN, pad=15)
    ax2.set_xticks(quarters)
    ax2.set_xticklabels(quarter_labels)
    ax2.legend(loc='upper left', fontsize=9)
    ax2.set_ylim(0, 160)

    # Add growth annotation
    ax2.annotate('Scales with\ndemand', xy=(10, 35), fontsize=9, color=AZURE_GREEN,
                 ha='center')

    # Key differences text box
    fig.text(0.5, 0.02,
             'CapEx: Large upfront investment, periodic refresh cycles | '
             'OpEx: Pay-as-you-go, scales with business needs',
             ha='center', fontsize=10, color='#666666', style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.12)

    return fig


def main():
    """Generate and save the CapEx vs OpEx chart."""

    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating CapEx vs OpEx Comparison Chart...")

    fig = create_capex_opex_chart()

    output_path = output_dir / 'capex-opex-comparison.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    plt.close(fig)
    print("✅ Chart generated successfully!")


if __name__ == '__main__':
    main()
