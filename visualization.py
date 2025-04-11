# visualization.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

def draw_grid_with_legend(grid, path=None, show_text=False, cmap=None, colors=None, legend_labels=None):
    grid_np = np.array(grid)
    plt.figure(figsize=(14, 9))
    ax = plt.gca()
    im = ax.imshow(grid_np, cmap=cmap, interpolation="none")

    if path:
        y, x = zip(*path)
        ax.plot(x, y, color="red", linewidth=2, marker="o")

    if show_text:
        for i in range(grid_np.shape[0]):
            for j in range(grid_np.shape[1]):
                ax.text(
                    j,
                    i,
                    str(grid_np[i, j]),
                    ha="center",
                    va="center",
                    fontsize=6,
                    color="black",
                )

    plt.grid(True, which="both", color="gray", linestyle="--", linewidth=0.5)
    plt.xticks(range(grid_np.shape[1]))
    plt.yticks(range(grid_np.shape[0]))
    plt.title("Map and Path", fontsize=14)

    legend_elements = [
        Patch(facecolor=colors[val], edgecolor="black", label=f"{val}: {desc}")
        for val, desc in legend_labels.items()
    ]

    plt.legend(
        handles=legend_elements,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=4,
        fontsize=10,
        frameon=False,
    )

    plt.tight_layout()
    plt.show()
