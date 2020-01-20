import matplotlib.pyplot as plt


def plot_points(points, figsize=(12, 12)):
    """Plots a list of points"""
    fig, ax = plt.subplots(figsize=figsize)

    for pt in points:
        coords = (pt.x, pt.y)
        ax.plot(pt.x, pt.y, 'ro')
        ax.annotate(coords, coords)
    plt.show()
