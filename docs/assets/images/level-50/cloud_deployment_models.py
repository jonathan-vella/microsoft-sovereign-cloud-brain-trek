#!/usr/bin/env python3
"""Cloud Deployment Models diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_PURPLE = '#7b1fa2'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 7.5, 'Cloud Deployment Models',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Define the 4 model boxes
    models = [
        {
            'x': 1.5, 'y': 4.5, 'title': '[Cloud] Public Cloud', 'color': '#e3f2fd', 'edge': AZURE_BLUE,
            'items': ['Shared Infrastructure', 'Internet Access', 'Pay-per-Use']
        },
        {
            'x': 5, 'y': 4.5, 'title': '[Building] Private Cloud', 'color': '#fff3e0', 'edge': AZURE_ORANGE,
            'items': ['Dedicated Infrastructure', 'On-Premises or Hosted', 'Full Control']
        },
        {
            'x': 8.5, 'y': 4.5, 'title': '🔗 Hybrid Cloud', 'color': '#e8f5e9', 'edge': AZURE_GREEN,
            'items': ['Public + Private', 'Unified Management', 'Workload Flexibility']
        },
        {
            'x': 12, 'y': 4.5, 'title': '[Global] Multi-Cloud', 'color': '#f3e5f5', 'edge': AZURE_PURPLE,
            'items': ['Multiple Providers', 'Best-of-Breed', 'Avoid Lock-in']
        }
    ]

    for model in models:
        # Background box
        box = FancyBboxPatch((model['x'] - 1.3, model['y'] - 2.2), 2.6, 3.2,
                              boxstyle="round,pad=0.1",
                              facecolor=model['color'], edgecolor=model['edge'], linewidth=2)
        ax.add_patch(box)

        # Title
        ax.text(model['x'], model['y'] + 0.7, model['title'],
                fontsize=10, fontweight='bold', ha='center', color=model['edge'])

        # Items
        for i, item in enumerate(model['items']):
            item_box = FancyBboxPatch((model['x'] - 1.1, model['y'] - 0.2 - i*0.6), 2.2, 0.5,
                                       boxstyle="round,pad=0.02", facecolor='white',
                                       edgecolor=model['edge'], linewidth=0.5, alpha=0.9)
            ax.add_patch(item_box)
            ax.text(model['x'], model['y'] + 0.05 - i*0.6, item,
                    fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Use case section at bottom
    use_cases_bg = FancyBboxPatch((0.5, 0.3), 13, 1.5, boxstyle="round,pad=0.1",
                                   facecolor='#F5F5F5', edgecolor=AZURE_DARK, linewidth=1)
    ax.add_patch(use_cases_bg)

    ax.text(7, 1.5, 'Common Use Cases', fontsize=11, fontweight='bold', ha='center', color=AZURE_DARK)

    use_cases = [
        (1.5, 'Startups, SaaS', AZURE_BLUE),
        (5, 'Regulated Industries', AZURE_ORANGE),
        (8.5, 'Enterprise IT', AZURE_GREEN),
        (12, 'Global Enterprises', AZURE_PURPLE)
    ]

    for x, text, color in use_cases:
        ax.text(x, 0.7, text, fontsize=8, ha='center', color=color, fontweight='bold')

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('cloud-deployment-models-overview.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated cloud-deployment-models-overview.svg")
    plt.close(fig)
