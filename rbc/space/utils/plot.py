import matplotlib.pyplot as plt

from .base import get_polygon_label


def plot_space(sp, figsize=(12, 12)):
    """Plots a list of spaces"""
    fig, ax = plt.subplots(figsize=figsize)

    # plot self's boundary without label
    handle_parent_polygons(sp, ax)

    plt.axis('scaled')
    plt.show()


def handle_parent_polygons(sp, ax):
    """Plot child polygons before parent polygons"""
    if hasattr(sp, 'plan'):
        if sp.plan:  # plat subspaces before sp
            subspace_classes = set()
            for label, subspace in sp.plan.items():
                handle_parent_polygons(subspace, ax)
                # subspace_classes.add(subspace.__class__)
            # Do not show labels for parent polygons
            add_space_to_plot(sp, ax, show_labels=False)
        else:
            add_space_to_plot(sp, ax, show_labels=True)


def add_space_to_plot(sp, ax, show_labels=False):
    """Add a Space object to the plot"""
    x, y = sp.exterior.xy
    ax.plot(x, y)
    if show_labels:
        plan_label = get_polygon_label(sp)
        ax.text(sp.centroid.x, sp.centroid.y, s=plan_label,
                horizontalalignment='center', verticalalignment='center')