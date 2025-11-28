#!/usr/bin/env python3
"""
Vector Embedding Process Visualization
L100-32: How text is converted to vector embeddings for RAG
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Output path
output_dir = "/workspaces/sov-cloud-brain-trek/docs/assets/images/level-100"
os.makedirs(output_dir, exist_ok=True)

fig, axes = plt.subplots(1, 3, figsize=(16, 6))
fig.suptitle("Vector Embedding Process for RAG Systems", fontsize=16, fontweight='bold', y=1.02)

# Chart 1: Text to Vector Pipeline
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("1. Text → Vector Pipeline", fontsize=12, fontweight='bold', pad=10)

# Pipeline steps
steps = [
    (5, 9, "📄 Raw Text", "#E8F4FD", "\"Azure Local enables\nhybrid cloud...\""),
    (5, 7, "🔤 Tokenization", "#FFF4E6", "['Azure', 'Local',\n'enables', 'hybrid'...]"),
    (5, 5, "🧠 Embedding Model", "#F3E8FF", "all-MiniLM-L6-v2\nor E5-large"),
    (5, 3, "📊 Vector Output", "#D4E9D7", "[0.023, -0.156, 0.892,\n..., 0.445]  (384-dim)"),
    (5, 1, "💾 Vector Database", "#FFE6E6", "Stored in Qdrant,\nChroma, or FAISS"),
]

for x, y, label, color, detail in steps:
    box = mpatches.FancyBboxPatch((x-2.2, y-0.7), 4.4, 1.4,
                                   boxstyle="round,pad=0.05",
                                   facecolor=color, edgecolor='#333', linewidth=1.5)
    ax1.add_patch(box)
    ax1.text(x, y+0.2, label, ha='center', va='center', fontsize=10, fontweight='bold')
    ax1.text(x, y-0.3, detail, ha='center', va='center', fontsize=8, style='italic')

# Arrows between steps
for i in range(len(steps)-1):
    ax1.annotate('', xy=(5, steps[i+1][1]+0.7), xytext=(5, steps[i][1]-0.7),
                arrowprops=dict(arrowstyle='->', color='#0078D4', lw=2))

# Chart 2: Semantic Similarity in Vector Space
ax2 = axes[1]
ax2.set_title("2. Semantic Similarity in Vector Space", fontsize=12, fontweight='bold', pad=10)

# Generate sample points for demonstration
np.random.seed(42)
# Cluster 1: Azure/Cloud topics (blue)
cloud_x = np.random.normal(2, 0.5, 8)
cloud_y = np.random.normal(3, 0.5, 8)
# Cluster 2: Security topics (purple)
security_x = np.random.normal(5, 0.5, 6)
security_y = np.random.normal(2, 0.5, 6)
# Cluster 3: Data topics (green)
data_x = np.random.normal(4, 0.4, 5)
data_y = np.random.normal(5, 0.4, 5)
# Query point (red star)
query_x, query_y = 2.3, 3.2

ax2.scatter(cloud_x, cloud_y, c='#0078D4', s=100, alpha=0.7, label='Cloud/Azure docs')
ax2.scatter(security_x, security_y, c='#5C2D91', s=100, alpha=0.7, label='Security docs')
ax2.scatter(data_x, data_y, c='#107C10', s=100, alpha=0.7, label='Data docs')
ax2.scatter(query_x, query_y, c='#D13438', s=200, marker='*', label='Query', zorder=5)

# Draw similarity radius
circle = plt.Circle((query_x, query_y), 1.0, fill=False, color='#D13438', linestyle='--', linewidth=2)
ax2.add_patch(circle)
ax2.text(query_x+0.1, query_y-1.3, "Top-k\nnearest", fontsize=9, color='#D13438', ha='center')

ax2.set_xlabel("Embedding Dimension 1", fontsize=10)
ax2.set_ylabel("Embedding Dimension 2", fontsize=10)
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(0, 7)
ax2.set_ylim(0, 7)
ax2.grid(True, alpha=0.3)

# Chart 3: Embedding Model Comparison
ax3 = axes[2]
ax3.set_title("3. Embedding Model Comparison", fontsize=12, fontweight='bold', pad=10)

models = ['all-MiniLM\n-L6-v2', 'E5-large\n-v2', 'BGE-large\n-en', 'text-embedding\n-3-small', 'Instructor\n-XL']
dimensions = [384, 1024, 1024, 1536, 768]
quality = [78, 89, 87, 91, 88]  # Approximate MTEB scores
speed = [95, 45, 50, 30, 35]  # Relative speed (higher = faster)

x = np.arange(len(models))
width = 0.35

bars1 = ax3.bar(x - width/2, quality, width, label='Quality (MTEB %)', color='#0078D4', alpha=0.8)
bars2 = ax3.bar(x + width/2, speed, width, label='Speed (relative)', color='#107C10', alpha=0.8)

ax3.set_ylabel('Score', fontsize=10)
ax3.set_xticks(x)
ax3.set_xticklabels(models, fontsize=9)
ax3.legend(loc='upper right', fontsize=9)
ax3.set_ylim(0, 100)
ax3.axhline(y=85, color='#FF8C00', linestyle='--', alpha=0.7, label='Good threshold')

# Add dimension labels
for i, (model, dim) in enumerate(zip(models, dimensions)):
    ax3.text(i, 5, f"{dim}d", ha='center', fontsize=8, color='white', fontweight='bold')

ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

plt.tight_layout()

# Save
output_path = f"{output_dir}/vector-embedding-process"
plt.savefig(f"{output_path}.svg", format='svg', dpi=150, bbox_inches='tight')
plt.savefig(f"{output_path}.png", format='png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✅ Generated: {output_path}.svg")
print(f"✅ Generated: {output_path}.png")
