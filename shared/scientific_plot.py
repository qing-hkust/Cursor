"""
Default matplotlib styling for scientific figures.

Importing this module applies the style globally (see end of file). You can
also call apply_scientific_style() explicitly, or use scientific_plot_context
for a temporary override.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def _rc_scientific() -> dict:
    return {
        # Font: Arial 18 pt (fallbacks if Arial is unavailable)
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "Liberation Sans"],
        "font.size": 18,
        "axes.titlesize": 18,
        "axes.labelsize": 18,
        "xtick.labelsize": 18,
        "ytick.labelsize": 18,
        "legend.fontsize": 18,
        # Line weight 1.5 pt (matplotlib uses points for linewidth)
        "lines.linewidth": 1.5,
        "lines.markersize": 8,
        "axes.linewidth": 1.5,
        # Ticks inside the axes only
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.size": 7,
        "ytick.major.size": 7,
        "xtick.minor.size": 4,
        "ytick.minor.size": 4,
        # Legend inside axes by default (caller sets loc='best' to reduce overlap)
        "legend.loc": "best",
        "legend.frameon": True,
        "legend.fancybox": True,
        "legend.framealpha": 0.92,
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
    }


def apply_scientific_style() -> None:
    """Apply template to the global matplotlib rcParams (affects all new figures)."""
    mpl.rcParams.update(_rc_scientific())


@contextmanager
def scientific_plot_context() -> Iterator[None]:
    """Temporarily apply scientific style; restore previous rcParams on exit."""
    with mpl.rc_context(rc=_rc_scientific()):
        yield


def _linear_endpoint_ticks(
    ax: mpl.axes.Axes,
    num_x: int = 5,
    num_y: int = 5,
) -> None:
    """Place major ticks at both ends of each linear axis (labelled range endpoints)."""
    for axis, get_lim, set_ticks, get_scale in (
        (ax.xaxis, ax.get_xlim, ax.set_xticks, ax.get_xscale),
        (ax.yaxis, ax.get_ylim, ax.set_yticks, ax.get_yscale),
    ):
        if get_scale() != "linear":
            continue
        lo, hi = get_lim()
        if not np.isfinite(lo) or not np.isfinite(hi) or lo == hi:
            continue
        n = num_x if axis is ax.xaxis else num_y
        ticks = np.linspace(lo, hi, num=max(2, n))
        set_ticks(ticks)


def legend_inside_axes(
    ax: mpl.axes.Axes,
    *args,
    **kwargs,
) -> mpl.legend.Legend:
    """
    Legend drawn inside the plotting area. Uses loc='best' by default so
    matplotlib picks a position that usually avoids line overlap.
    """
    kw = {"loc": "best", "framealpha": 0.92}
    kw.update(kwargs)
    return ax.legend(*args, **kw)


def finalize_scientific_axes(
    ax: mpl.axes.Axes | None = None,
    *,
    num_xticks: int = 5,
    num_yticks: int = 5,
) -> None:
    """
    After plotting data: ensure linear axes have labelled ticks at both ends.
    """
    axes = [ax] if ax is not None else plt.gcf().axes
    for a in axes:
        _linear_endpoint_ticks(a, num_x=num_xticks, num_y=num_yticks)


# Default for any script that imports this module (one-line setup).
apply_scientific_style()
