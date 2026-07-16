#!/usr/bin/env python3
"""Example figure using the scientific plot template."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))

from scientific_plot import finalize_scientific_axes, legend_inside_axes


def main() -> None:
    x = np.linspace(0, 2 * np.pi, 200)
    y1 = np.sin(x)
    y2 = 0.7 * np.cos(x)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(x, y1, label=r"$\sin(x)$")
    ax.plot(x, y2, label=r"$0.7\cos(x)$")

    ax.set_xlabel(r"$x$ (rad)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Scientific plot template example")

    legend_inside_axes(ax)

    finalize_scientific_axes(ax, num_xticks=5, num_yticks=5)

    fig.tight_layout()
    out = Path(__file__).resolve().parent / "example_scientific_plot.png"
    fig.savefig(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
