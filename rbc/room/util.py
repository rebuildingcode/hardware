import random
import matplotlib.pyplot as plt

from ..point import Point


def plot_rooms(rooms, figsize=(12, 12), labels=True):
    """Plots a list of rooms"""
    fig, ax = plt.subplots(figsize=figsize)
    for room in rooms:
        x, y = room.exterior.xy
        ax.plot(x, y)
        ax.text(room.centroid.x, room.centroid.y, s=room.room_type,
                horizontalalignment='center', verticalalignment='center')
    plt.show()


def random_rectangle(max_x, max_y, min_x=0, min_y=0, min_area=None):
    """Return list of Points that form a rectangle"""
    # prevent sides with length of zero
    min_x = max(min_x, 1)
    min_y = max(min_y, 1)

    if min_area:
        first_var = random.choice(['x', 'y'])
        if first_var == 'x':
            x = random.randint(min_x, max_x)
            min_y = min(max(min_y, min_area // x + 1), max_y)
            y = random.randint(min_y, max_y)
        else:
            y = random.randint(min_y, max_y)
            min_x = min(max(min_x, min_area // y + 1), max_x)
            x = random.randint(min_x, max_x)
    else:
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)

    pt1 = Point(0, 0, 0)
    pt2 = Point(0, y, 0)
    pt3 = Point(x, y, 0)
    pt4 = Point(x, 0, 0)

    return [pt1, pt2, pt3, pt4]
