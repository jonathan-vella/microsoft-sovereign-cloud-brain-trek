#!/usr/bin/env python3
"""Authentication vs Authorization Flow diagram for Level 50"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Wedge
import numpy as np

# Azure color palette
AZURE_BLUE = '#0078D4'
AZURE_DARK = '#004578'
AZURE_GREEN = '#107C10'
AZURE_RED = '#D13438'
AUTH_COLOR = '#bbdefb'
AUTHZ_COLOR = '#c8e6c9'
SUCCESS_COLOR = '#a5d6a7'
DENIED_COLOR = '#ffcdd2'

def create_diagram():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_aspect('equal')

    # Title
    ax.text(7, 5.5, 'Authentication vs Authorization Flow',
            fontsize=16, fontweight='bold', ha='center', color=AZURE_DARK)

    # User icon
    user = Circle((1, 3), 0.5, facecolor='white', edgecolor=AZURE_DARK, linewidth=2)
    ax.add_patch(user)
    ax.text(1, 3, '[User]', fontsize=16, ha='center', va='center')
    ax.text(1, 2.2, 'User', fontsize=9, ha='center', color=AZURE_DARK)

    # Authentication box
    auth = FancyBboxPatch((2.5, 2.4), 2, 1.2, boxstyle="round,pad=0.02",
                           facecolor=AUTH_COLOR, edgecolor=AZURE_BLUE, linewidth=2)
    ax.add_patch(auth)
    ax.text(3.5, 3.3, '[Auth]', fontsize=14, ha='center', va='center')
    ax.text(3.5, 2.8, 'Authentication', fontsize=10, fontweight='bold', ha='center', color=AZURE_DARK)
    ax.text(3.5, 4.0, '"Who are you?"', fontsize=9, fontstyle='italic', ha='center', color=AZURE_BLUE)

    # Verify Identity diamond
    diamond_x, diamond_y = 6, 3
    diamond = plt.Polygon([(diamond_x, diamond_y + 0.6), (diamond_x + 0.7, diamond_y),
                           (diamond_x, diamond_y - 0.6), (diamond_x - 0.7, diamond_y)],
                          facecolor='white', edgecolor=AZURE_DARK, linewidth=2)
    ax.add_patch(diamond)
    ax.text(diamond_x, diamond_y, 'Verify\nIdentity', fontsize=7, ha='center', va='center', color=AZURE_DARK)

    # Authorization box
    authz = FancyBboxPatch((7.5, 2.4), 2, 1.2, boxstyle="round,pad=0.02",
                            facecolor=AUTHZ_COLOR, edgecolor=AZURE_GREEN, linewidth=2)
    ax.add_patch(authz)
    ax.text(8.5, 3.3, '[Ticket]', fontsize=14, ha='center', va='center')
    ax.text(8.5, 2.8, 'Authorization', fontsize=10, fontweight='bold', ha='center', color=AZURE_DARK)
    ax.text(8.5, 4.0, '"What can you do?"', fontsize=9, fontstyle='italic', ha='center', color=AZURE_GREEN)

    # Check Permissions diamond
    perm_x, perm_y = 11, 3
    perm_diamond = plt.Polygon([(perm_x, perm_y + 0.6), (perm_x + 0.7, perm_y),
                                (perm_x, perm_y - 0.6), (perm_x - 0.7, perm_y)],
                               facecolor='white', edgecolor=AZURE_DARK, linewidth=2)
    ax.add_patch(perm_diamond)
    ax.text(perm_x, perm_y, 'Check\nPerms', fontsize=7, ha='center', va='center', color=AZURE_DARK)

    # Access Resource box
    access = FancyBboxPatch((12.3, 2.4), 1.4, 1.2, boxstyle="round,pad=0.02",
                             facecolor=SUCCESS_COLOR, edgecolor=AZURE_GREEN, linewidth=2)
    ax.add_patch(access)
    ax.text(13, 3, '[OK]\nAccess\nResource', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Denied boxes
    denied1 = FancyBboxPatch((5.3, 0.8), 1.4, 0.8, boxstyle="round,pad=0.02",
                              facecolor=DENIED_COLOR, edgecolor=AZURE_RED, linewidth=2)
    ax.add_patch(denied1)
    ax.text(6, 1.2, '[X] Denied', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    denied2 = FancyBboxPatch((10.3, 0.8), 1.4, 0.8, boxstyle="round,pad=0.02",
                              facecolor=DENIED_COLOR, edgecolor=AZURE_RED, linewidth=2)
    ax.add_patch(denied2)
    ax.text(11, 1.2, '[X] Denied', fontsize=8, ha='center', va='center', color=AZURE_DARK)

    # Arrows
    # User to Auth
    ax.annotate('', xy=(2.5, 3), xytext=(1.5, 3),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # Auth to Verify
    ax.annotate('', xy=(5.3, 3), xytext=(4.5, 3),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # Verify to Authz (Valid)
    ax.annotate('', xy=(7.5, 3), xytext=(6.7, 3),
                arrowprops=dict(arrowstyle='->', color=AZURE_GREEN, lw=2))
    ax.text(7.1, 3.3, 'Valid', fontsize=8, color=AZURE_GREEN)

    # Verify to Denied (Invalid)
    ax.annotate('', xy=(6, 1.6), xytext=(6, 2.4),
                arrowprops=dict(arrowstyle='->', color=AZURE_RED, lw=2))
    ax.text(5.5, 2, 'Invalid', fontsize=8, color=AZURE_RED)

    # Authz to Check Perms
    ax.annotate('', xy=(10.3, 3), xytext=(9.5, 3),
                arrowprops=dict(arrowstyle='->', color=AZURE_DARK, lw=2))

    # Check Perms to Access (Allowed)
    ax.annotate('', xy=(12.3, 3), xytext=(11.7, 3),
                arrowprops=dict(arrowstyle='->', color=AZURE_GREEN, lw=2))
    ax.text(12, 3.3, 'Allowed', fontsize=8, color=AZURE_GREEN)

    # Check Perms to Denied (Not Allowed)
    ax.annotate('', xy=(11, 1.6), xytext=(11, 2.4),
                arrowprops=dict(arrowstyle='->', color=AZURE_RED, lw=2))
    ax.text(10.3, 2, 'Not\nAllowed', fontsize=7, color=AZURE_RED)

    plt.tight_layout()
    return fig

if __name__ == '__main__':
    fig = create_diagram()
    fig.savefig('authentication-authorization-flow.svg', format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Generated authentication-authorization-flow.svg")
    plt.close(fig)
