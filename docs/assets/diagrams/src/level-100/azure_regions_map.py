#!/usr/bin/env python3
"""
Azure Sovereign Regions Geographic Map
Creates a world map showing Azure regions with sovereignty classifications.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
from pathlib import Path

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK_BLUE = '#004578'
AZURE_GREEN = '#107C10'
AZURE_ORANGE = '#FF8C00'
AZURE_RED = '#D13438'
AZURE_PURPLE = '#5C2D91'

# Azure regions with sovereignty classifications
AZURE_REGIONS = {
    # Global Public Cloud Regions (subset for clarity)
    'public': [
        {'name': 'East US', 'lat': 37.3719, 'lon': -79.8164},
        {'name': 'West US', 'lat': 37.783, 'lon': -122.417},
        {'name': 'Central US', 'lat': 41.5908, 'lon': -93.6208},
        {'name': 'North Europe', 'lat': 53.3478, 'lon': -6.2597},
        {'name': 'West Europe', 'lat': 52.3667, 'lon': 4.9},
        {'name': 'UK South', 'lat': 51.5074, 'lon': -0.1278},
        {'name': 'France Central', 'lat': 46.3772, 'lon': 2.373},
        {'name': 'Germany West Central', 'lat': 50.1109, 'lon': 8.6821},
        {'name': 'Switzerland North', 'lat': 47.4515, 'lon': 8.5644},
        {'name': 'Canada Central', 'lat': 43.653, 'lon': -79.383},
        {'name': 'Australia East', 'lat': -33.8688, 'lon': 151.2093},
        {'name': 'Japan East', 'lat': 35.6762, 'lon': 139.6503},
        {'name': 'Southeast Asia', 'lat': 1.3521, 'lon': 103.8198},
        {'name': 'Brazil South', 'lat': -23.5505, 'lon': -46.6333},
        {'name': 'UAE North', 'lat': 25.2048, 'lon': 55.2708},
        {'name': 'India Central', 'lat': 18.5204, 'lon': 73.8567},
        {'name': 'Korea Central', 'lat': 37.5665, 'lon': 126.978},
        {'name': 'South Africa North', 'lat': -26.2041, 'lon': 28.0473},
    ],
    # EU Data Boundary Regions
    'eu_boundary': [
        {'name': 'Sweden Central', 'lat': 59.3293, 'lon': 18.0686},
        {'name': 'Italy North', 'lat': 45.4642, 'lon': 9.19},
        {'name': 'Poland Central', 'lat': 52.2297, 'lon': 21.0122},
        {'name': 'Spain Central', 'lat': 40.4168, 'lon': -3.7038},
    ],
    # National/Sovereign Clouds
    'sovereign': [
        {'name': 'Azure Government (US)', 'lat': 38.8951, 'lon': -77.0364},
        {'name': 'Azure China', 'lat': 39.9042, 'lon': 116.4074},
    ],
    # Air-Gapped Regions
    'airgapped': [
        {'name': 'Azure Government Secret', 'lat': 38.0, 'lon': -80.0},
        {'name': 'Azure Government Top Secret', 'lat': 35.0, 'lon': -85.0},
    ],
}

# EU Data Boundary outline (approximate)
EU_BOUNDARY_COORDS = [
    (-10, 36), (0, 36), (10, 35), (25, 35), (35, 40), (30, 45),
    (30, 55), (35, 60), (30, 70), (25, 72), (10, 72), (-10, 60), (-10, 36)
]


def create_azure_regions_map():
    """Create a geographic map of Azure regions with sovereignty classifications."""

    fig = plt.figure(figsize=(16, 10))

    # Use Robinson projection for world view
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # Set global extent
    ax.set_global()

    # Add map features
    ax.add_feature(cfeature.OCEAN, facecolor='#E6F2FF', alpha=0.8)
    ax.add_feature(cfeature.LAND, facecolor='#F5F5F5', edgecolor='#CCCCCC', linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linestyle='-', linewidth=0.3, alpha=0.5, edgecolor='#999999')
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5, edgecolor='#666666')

    # Add EU Data Boundary shading
    eu_lons = [coord[0] for coord in EU_BOUNDARY_COORDS]
    eu_lats = [coord[1] for coord in EU_BOUNDARY_COORDS]
    ax.fill(eu_lons, eu_lats, transform=ccrs.PlateCarree(),
            facecolor=AZURE_PURPLE, alpha=0.15, edgecolor=AZURE_PURPLE,
            linewidth=2, linestyle='--', label='EU Data Boundary')

    # Plot regions by category
    marker_size = 80

    # Public cloud regions
    for region in AZURE_REGIONS['public']:
        ax.scatter(region['lon'], region['lat'],
                   transform=ccrs.PlateCarree(),
                   c=AZURE_BLUE, s=marker_size, marker='o',
                   edgecolors='white', linewidths=1.5, zorder=5)

    # EU Data Boundary regions
    for region in AZURE_REGIONS['eu_boundary']:
        ax.scatter(region['lon'], region['lat'],
                   transform=ccrs.PlateCarree(),
                   c=AZURE_PURPLE, s=marker_size, marker='o',
                   edgecolors='white', linewidths=1.5, zorder=5)

    # Sovereign cloud regions
    for region in AZURE_REGIONS['sovereign']:
        ax.scatter(region['lon'], region['lat'],
                   transform=ccrs.PlateCarree(),
                   c=AZURE_ORANGE, s=marker_size * 1.5, marker='s',
                   edgecolors='white', linewidths=2, zorder=6)

    # Air-gapped regions
    for region in AZURE_REGIONS['airgapped']:
        ax.scatter(region['lon'], region['lat'],
                   transform=ccrs.PlateCarree(),
                   c=AZURE_RED, s=marker_size * 1.5, marker='^',
                   edgecolors='white', linewidths=2, zorder=6)

    # Add legend
    legend_elements = [
        mpatches.Patch(facecolor=AZURE_BLUE, edgecolor='white', label='Azure Public Regions'),
        mpatches.Patch(facecolor=AZURE_PURPLE, edgecolor='white', label='EU Data Boundary Regions'),
        mpatches.Patch(facecolor=AZURE_ORANGE, edgecolor='white', label='Sovereign Clouds (Gov/China)'),
        mpatches.Patch(facecolor=AZURE_RED, edgecolor='white', label='Air-Gapped Regions'),
        mpatches.Patch(facecolor=AZURE_PURPLE, alpha=0.15, edgecolor=AZURE_PURPLE,
                       linestyle='--', label='EU Data Boundary Zone'),
    ]

    ax.legend(handles=legend_elements, loc='lower left', fontsize=10,
              framealpha=0.95, fancybox=True, shadow=True)

    # Title
    ax.set_title('Azure Global Regions with Sovereignty Classifications',
                 fontsize=16, fontweight='bold', color=AZURE_DARK_BLUE, pad=20)

    # Add subtitle
    fig.text(0.5, 0.02,
             'Sovereign clouds provide isolated environments for regulated workloads | '
             'EU Data Boundary ensures European data residency',
             ha='center', fontsize=10, color='#666666')

    plt.tight_layout()

    return fig


def main():
    """Generate and save the Azure regions map."""

    # Output directory (relative to the docs/assets structure)
    output_dir = Path(__file__).parent.parent.parent.parent / 'images' / 'level-100'
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating Azure Regions Geographic Map...")

    fig = create_azure_regions_map()

    # Save as SVG
    output_path = output_dir / 'azure-regions-map.svg'
    fig.savefig(output_path, format='svg', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path}")

    # Also save as PNG for fallback
    output_path_png = output_dir / 'azure-regions-map.png'
    fig.savefig(output_path_png, format='png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  ✓ Saved: {output_path_png}")

    plt.close(fig)

    print("\n✅ Azure regions map generated successfully!")


if __name__ == '__main__':
    main()
