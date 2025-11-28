#!/usr/bin/env python3
"""Azure Compute Options diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_LIGHT = '#E8F4FD'
LIGHT_ORANGE = '#FFF4E6'
LIGHT_GREEN = '#D4E9D7'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 8.5, '[Cloud] Azure Compute Options',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # IaaS Section
    iaas_bg = FancyBboxPatch((0.5, 4.5), 4, 3.5, boxstyle="round,pad=0.1",
                              facecolor=AZURE_LIGHT, edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(iaas_bg)
    ax.text(2.5, 7.7, 'Infrastructure (IaaS)', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_BLUE)

    iaas_services = [
        ('Virtual Machines', 'Full OS Control'),
        ('VM Scale Sets', 'Auto-scaling VMs')
    ]

    for i, (name, desc) in enumerate(iaas_services):
        y = 6.8 - i * 1.2
        box = FancyBboxPatch((0.8, y - 0.4), 3.4, 0.9, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_BLUE, linewidth=1.5)
        ax.add_patch(box)
        ax.text(2.5, y + 0.1, name, fontsize=9, fontweight='bold', ha='center', color=AZURE_DARK)
        ax.text(2.5, y - 0.2, desc, fontsize=8, ha='center', color=AZURE_DARK, alpha=0.8)

    # PaaS Section
    paas_bg = FancyBboxPatch((5, 4.5), 4, 3.5, boxstyle="round,pad=0.1",
                              facecolor=LIGHT_ORANGE, edgecolor=AZURE_ORANGE, linewidth=2)
    ax.add_patch(paas_bg)
    ax.text(7, 7.7, 'Platform (PaaS)', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_ORANGE)

    paas_services = [
        ('App Service', 'Web Apps'),
        ('Container Instances', 'Simple Containers'),
        ('Kubernetes Service', 'Container Orchestration')
    ]

    for i, (name, desc) in enumerate(paas_services):
        y = 6.8 - i * 0.85
        box = FancyBboxPatch((5.3, y - 0.3), 3.4, 0.7, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_ORANGE, linewidth=1.5)
        ax.add_patch(box)
        ax.text(7, y + 0.05, name, fontsize=9, fontweight='bold', ha='center', color=AZURE_DARK)
        ax.text(7, y - 0.2, desc, fontsize=7, ha='center', color=AZURE_DARK, alpha=0.8)

    # Serverless Section
    serverless_bg = FancyBboxPatch((9.5, 4.5), 4, 3.5, boxstyle="round,pad=0.1",
                                    facecolor=LIGHT_GREEN, edgecolor=AZURE_GREEN, linewidth=2)
    ax.add_patch(serverless_bg)
    ax.text(11.5, 7.7, 'Serverless', fontsize=11, fontweight='bold',
            ha='center', color=AZURE_GREEN)

    serverless_services = [
        ('Azure Functions', 'Event-driven'),
        ('Logic Apps', 'Workflows')
    ]

    for i, (name, desc) in enumerate(serverless_services):
        y = 6.8 - i * 1.2
        box = FancyBboxPatch((9.8, y - 0.4), 3.4, 0.9, boxstyle="round,pad=0.02",
                              facecolor='white', edgecolor=AZURE_GREEN, linewidth=1.5)
        ax.add_patch(box)
        ax.text(11.5, y + 0.1, name, fontsize=9, fontweight='bold', ha='center', color=AZURE_DARK)
        ax.text(11.5, y - 0.2, desc, fontsize=8, ha='center', color=AZURE_DARK, alpha=0.8)

    # Arrows showing progression
    arrow1 = FancyArrowPatch((4.6, 6), (4.9, 6), arrowstyle='-|>', mutation_scale=15,
                              fc=AZURE_DARK, ec=AZURE_DARK, linewidth=2)
    ax.add_patch(arrow1)
    ax.text(4.75, 6.5, 'More\nControl', fontsize=7, ha='center', va='bottom', color=AZURE_DARK)

    arrow2 = FancyArrowPatch((9.1, 6), (9.4, 6), arrowstyle='-|>', mutation_scale=15,
                              fc=AZURE_DARK, ec=AZURE_DARK, linewidth=2)
    ax.add_patch(arrow2)
    ax.text(9.25, 6.5, 'Less\nMgmt', fontsize=7, ha='center', va='bottom', color=AZURE_DARK)

    # Comparison section at bottom
    compare_bg = FancyBboxPatch((0.5, 0.5), 13, 3.5, boxstyle="round,pad=0.1",
                                 facecolor='#F5F5F5', edgecolor=AZURE_DARK, linewidth=1)
    ax.add_patch(compare_bg)

    ax.text(7, 3.6, 'When to Use Each', fontsize=12, fontweight='bold', ha='center', color=AZURE_DARK)

    comparisons = [
        (2.5, 'IaaS', ['Need full control', 'Lift & shift migrations', 'Custom configurations'], AZURE_BLUE),
        (7, 'PaaS', ['Focus on code, not infra', 'Rapid development', 'Managed runtimes'], AZURE_ORANGE),
        (11.5, 'Serverless', ['Event-driven workloads', 'Pay per execution', 'Auto-scale to zero'], AZURE_GREEN)
    ]

    for x, title, items, color in comparisons:
        ax.text(x, 3.0, title, fontsize=10, fontweight='bold', ha='center', color=color)
        for i, item in enumerate(items):
            ax.text(x, 2.4 - i*0.55, f'• {item}', fontsize=8, ha='center', color=AZURE_DARK)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('azure-compute-options.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated azure-compute-options.svg")
    plt.close(fig)
