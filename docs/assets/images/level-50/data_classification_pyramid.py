#!/usr/bin/env python3
"""Data Classification Pyramid diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Polygon
import numpy as np

# Colors for classification levels
RESTRICTED_COLOR = '#ffcdd2'
RESTRICTED_EDGE = '#c62828'
CONFIDENTIAL_COLOR = '#ffe0b2'
CONFIDENTIAL_EDGE = '#ef6c00'
INTERNAL_COLOR = '#fff9c4'
INTERNAL_EDGE = '#f9a825'
PUBLIC_COLOR = '#c8e6c9'
PUBLIC_EDGE = '#2e7d32'
AZURE_DARK = '#004578'

def create_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(6, 7.5, '[Chart] Data Classification Pyramid',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # Define pyramid levels (from top to bottom)
    levels = [
        {'y': 5.8, 'width': 2, 'label': '[R] Restricted', 'desc': 'Severe damage if disclosed',
         'color': RESTRICTED_COLOR, 'edge': RESTRICTED_EDGE, 'x': 6},
        {'y': 4.8, 'width': 3.5, 'label': '[O] Confidential', 'desc': 'Could cause harm',
         'color': CONFIDENTIAL_COLOR, 'edge': CONFIDENTIAL_EDGE, 'x': 6},
        {'y': 3.8, 'width': 5, 'label': '[Y] Internal', 'desc': 'Internal use only',
         'color': INTERNAL_COLOR, 'edge': INTERNAL_EDGE, 'x': 6},
        {'y': 2.8, 'width': 6.5, 'label': '[G] Public', 'desc': 'No harm if disclosed',
         'color': PUBLIC_COLOR, 'edge': PUBLIC_EDGE, 'x': 6}
    ]

    for level in levels:
        box = FancyBboxPatch((level['x'] - level['width']/2, level['y'] - 0.4),
                              level['width'], 0.8, boxstyle="round,pad=0.02",
                              facecolor=level['color'], edgecolor=level['edge'], linewidth=2)
        ax.add_patch(box)
        ax.text(level['x'], level['y'] + 0.05, level['label'],
                fontsize=10, fontweight='bold', ha='center', va='center', color=AZURE_DARK)
        ax.text(level['x'], level['y'] - 0.2, level['desc'],
                fontsize=8, ha='center', va='center', color=AZURE_DARK, alpha=0.8)

    # Arrows showing flow
    for i in range(len(levels) - 1):
        ax.annotate('', xy=(6, levels[i+1]['y'] + 0.4), xytext=(6, levels[i]['y'] - 0.4),
                    arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=1.5))

    # Protection requirements on the right
    ax.text(10, 6.0, 'Highest\nProtection', fontsize=9, ha='center', color=RESTRICTED_EDGE, fontweight='bold')
    ax.text(10, 2.8, 'Basic\nControls', fontsize=9, ha='center', color=PUBLIC_EDGE, fontweight='bold')
    ax.annotate('', xy=(10, 3.3), xytext=(10, 5.5),
                arrowprops=dict(arrowstyle='<->', color=AZURE_DARK, lw=2))

    # Examples on the left
    examples = [
        (2, 5.8, 'PII, Credentials, Trade Secrets', RESTRICTED_EDGE),
        (2, 4.8, 'Financial Data, HR Records', CONFIDENTIAL_EDGE),
        (2, 3.8, 'Policies, Procedures', INTERNAL_EDGE),
        (2, 2.8, 'Marketing Materials, Press Releases', PUBLIC_EDGE)
    ]

    for x, y, text, color in examples:
        ax.text(x, y, f'• {text}', fontsize=8, ha='left', va='center', color=color)

    # Bottom note
    ax.text(6, 1.5, 'Each level requires specific handling procedures, access controls, and protection measures',
            fontsize=9, fontstyle='italic', ha='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('data-classification-pyramid.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated data-classification-pyramid.svg")
    plt.close(fig)
