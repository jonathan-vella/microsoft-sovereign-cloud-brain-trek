#!/usr/bin/env python3
"""
Generate Azure Core Services Categories diagram.
Shows the major service categories in Microsoft Azure.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "images" / "level-50"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Azure service categories with icons and colors
categories = [
    {"name": "Compute", "icon": "💻", "color": "#0078D4",
     "services": ["Virtual Machines", "App Service", "Functions", "Kubernetes"]},
    {"name": "Storage", "icon": "💾", "color": "#00BCF2",
     "services": ["Blob Storage", "Files", "Disks", "Data Lake"]},
    {"name": "Networking", "icon": "🌐", "color": "#50E6FF",
     "services": ["Virtual Network", "Load Balancer", "VPN Gateway", "CDN"]},
    {"name": "Databases", "icon": "🗄️", "color": "#773ADC",
     "services": ["SQL Database", "Cosmos DB", "PostgreSQL", "Redis"]},
    {"name": "AI & ML", "icon": "🤖", "color": "#E3008C",
     "services": ["OpenAI Service", "Machine Learning", "Cognitive Services"]},
    {"name": "Security", "icon": "🔒", "color": "#107C10",
     "services": ["Entra ID", "Key Vault", "Defender", "Sentinel"]},
    {"name": "Analytics", "icon": "📊", "color": "#FF8C00",
     "services": ["Synapse", "Data Factory", "Stream Analytics", "Power BI"]},
    {"name": "Integration", "icon": "🔗", "color": "#FFB900",
     "services": ["Logic Apps", "API Management", "Service Bus", "Event Grid"]},
]

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 10))

    # Central Azure logo
    center_x, center_y = 7, 5
    center_circle = plt.Circle((center_x, center_y), 1.2,
                                facecolor='#0078D4', edgecolor='white', linewidth=3)
    ax.add_patch(center_circle)
    ax.text(center_x, center_y, "☁️\nAzure", ha='center', va='center',
            fontsize=14, fontweight='bold', color='white')

    # Position categories around the center
    n = len(categories)
    radius = 3.5

    for i, cat in enumerate(categories):
        angle = (2 * 3.14159 * i / n) - (3.14159 / 2)  # Start from top
        x = center_x + radius * 1.3 * (1 if i < 4 else -1) * abs(((i % 4) - 1.5) / 1.5)
        y = center_y + radius * (1 - abs((i % 4) - 1.5) / 2) * (1 if i < 2 or i > 5 else -1)

        # Adjust positions for better layout
        positions = [
            (4, 8.5), (10, 8.5), (12.5, 5), (10, 1.5),
            (4, 1.5), (1.5, 5), (2.5, 7), (11.5, 7)
        ]
        x, y = positions[i]

        # Draw category box
        box_width = 2.8
        box_height = 2.2
        rect = mpatches.FancyBboxPatch(
            (x - box_width/2, y - box_height/2), box_width, box_height,
            boxstyle="round,pad=0.02,rounding_size=0.3",
            facecolor=cat["color"],
            edgecolor="white",
            linewidth=2,
            alpha=0.9
        )
        ax.add_patch(rect)

        # Category name and icon
        ax.text(x, y + 0.5, f"{cat['icon']}", ha='center', va='center', fontsize=18)
        ax.text(x, y, cat["name"], ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        # Services (smaller text)
        services_text = "\n".join(cat["services"][:3])
        ax.text(x, y - 0.7, services_text, ha='center', va='top',
                fontsize=7, color='white', alpha=0.9)

        # Draw connection line to center
        ax.plot([center_x, x], [center_y, y],
                color='#cccccc', linewidth=1.5, linestyle='--', alpha=0.5, zorder=0)

    # Set up axes
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.set_title("Microsoft Azure Core Service Categories",
                 fontsize=18, fontweight='bold', pad=20, color='#333333')

    # Subtitle
    ax.text(7, -0.3, "Primary service categories for cloud solutions",
            ha='center', fontsize=10, color='#666666', style='italic')

    plt.tight_layout()

    # Save
    output_file = OUTPUT_DIR / "azure-service-categories.svg"
    plt.savefig(output_file, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none', dpi=150)
    plt.savefig(OUTPUT_DIR / "azure-service-categories.png", format='png',
                bbox_inches='tight', facecolor='white', edgecolor='none', dpi=150)

    print(f"✅ Generated: {output_file}")
    plt.close()

if __name__ == "__main__":
    create_diagram()
