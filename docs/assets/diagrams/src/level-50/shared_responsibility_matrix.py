#!/usr/bin/env python3
"""
Generate Shared Responsibility Matrix diagram for cloud service models.
Shows which layers are managed by customer vs provider in IaaS/PaaS/SaaS.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "images" / "level-50"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Define layers (bottom to top)
layers = [
    "Networking",
    "Storage",
    "Servers",
    "Virtualization",
    "Operating System",
    "Middleware",
    "Runtime",
    "Applications",
    "Data"
]

# Define models
models = ["On-Premises", "IaaS", "PaaS", "SaaS"]

# Responsibility matrix: 0 = Provider, 1 = Customer
# Rows: layers (bottom to top), Columns: models
responsibility = np.array([
    [1, 0, 0, 0],  # Networking
    [1, 0, 0, 0],  # Storage
    [1, 0, 0, 0],  # Servers
    [1, 0, 0, 0],  # Virtualization
    [1, 1, 0, 0],  # Operating System
    [1, 1, 0, 0],  # Middleware
    [1, 1, 0, 0],  # Runtime
    [1, 1, 1, 0],  # Applications
    [1, 1, 1, 1],  # Data
])

# Colors - Azure palette
CUSTOMER_COLOR = "#0078D4"  # Azure Blue
PROVIDER_COLOR = "#107C10"  # Azure Green

def create_matrix():
    fig, ax = plt.subplots(figsize=(10, 8))

    # Create the heatmap
    for i, layer in enumerate(layers):
        for j, model in enumerate(models):
            color = CUSTOMER_COLOR if responsibility[i, j] == 1 else PROVIDER_COLOR
            rect = mpatches.FancyBboxPatch(
                (j + 0.05, i + 0.05), 0.9, 0.9,
                boxstyle="round,pad=0.02,rounding_size=0.1",
                facecolor=color,
                edgecolor="white",
                linewidth=2
            )
            ax.add_patch(rect)

            # Add responsibility text
            text = "You" if responsibility[i, j] == 1 else "Provider"
            ax.text(j + 0.5, i + 0.5, text,
                   ha='center', va='center',
                   fontsize=10, fontweight='bold', color='white')

    # Set up axes
    ax.set_xlim(0, len(models))
    ax.set_ylim(0, len(layers))
    ax.set_aspect('equal')

    # Labels
    ax.set_xticks([i + 0.5 for i in range(len(models))])
    ax.set_xticklabels(models, fontsize=12, fontweight='bold')
    ax.set_yticks([i + 0.5 for i in range(len(layers))])
    ax.set_yticklabels(layers, fontsize=11)

    # Move x-axis to top
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    # Remove spines
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Title
    ax.set_title("Cloud Shared Responsibility Matrix\n", fontsize=16, fontweight='bold', pad=20)

    # Legend
    customer_patch = mpatches.Patch(color=CUSTOMER_COLOR, label='Customer Responsibility')
    provider_patch = mpatches.Patch(color=PROVIDER_COLOR, label='Provider Responsibility')
    ax.legend(handles=[customer_patch, provider_patch],
              loc='upper center', bbox_to_anchor=(0.5, -0.05),
              ncol=2, fontsize=10, frameon=False)

    # Add arrow showing "More Control" → "Less Management"
    ax.annotate('', xy=(3.8, 9.5), xytext=(-0.3, 9.5),
                arrowprops=dict(arrowstyle='->', color='#666666', lw=2))
    ax.text(1.75, 9.7, 'Less Management Overhead →', ha='center', fontsize=9, color='#666666')

    plt.tight_layout()

    # Save
    output_file = OUTPUT_DIR / "shared-responsibility-matrix.svg"
    plt.savefig(output_file, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none', dpi=150)
    plt.savefig(OUTPUT_DIR / "shared-responsibility-matrix.png", format='png',
                bbox_inches='tight', facecolor='white', edgecolor='none', dpi=150)

    print(f"✅ Generated: {output_file}")
    plt.close()

if __name__ == "__main__":
    create_matrix()
