import matplotlib.pyplot as plt


def plot_axial_member(mem, figsize=(12, 12), include_loads=False):
    """Plots an axial member"""
    fig, ax = plt.subplots(figsize=figsize)

    y = [pt.z for pt in mem.points]
    x = [0 for pt in y]

    ax.plot(x, y)
    ax.text(x[0], y[0], s='BASE',
            horizontalalignment='center',
            verticalalignment='top')

    # if include_loads:
    #     for l in mem.load_data:
    #         load_loc = l['location']/100 * mem.height + 0.25
    #         arrow_dy = 0.25

    #         ax.text(x[0], y=load_loc + arrow_dy + 0.25,
    #                 s=l['load'].magnitude,
    #                 horizontalalignment='center',
    #                 verticalalignment='bottom')

    #         ax.arrow(x[0], y=load_loc, dx=0, dy=arrow_dy,
    #                  shape='full', width=0.0005, head_length=0.1,
    #                  label=l['load'].magnitude)
    #     plt.ylim((y[0] - 1, y[-1] + 2))

    plt.show()
