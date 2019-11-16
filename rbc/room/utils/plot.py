import matplotlib.pyplot as plt


def plot_rooms(rooms, figsize=(12, 12), labels=True):
    """Plots a list of rooms"""
    fig, ax = plt.subplots(figsize=figsize)
    for room in rooms:
        x, y = room.exterior.xy
        ax.plot(x, y)
        ax.text(room.centroid.x, room.centroid.y, s=room.room_type,
                horizontalalignment='center', verticalalignment='center')
    plt.show()
