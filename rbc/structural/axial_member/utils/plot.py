import matplotlib.pyplot as plt


def plot_axial_member(mem, figsize=(12, 12), include_loads=False):
    """Plots an axial member"""
    fig, ax = plt.subplots(figsize=figsize)

    y = [pt.z for pt in mem.points]
    x = [0 for pt in y]

    ax.plot(x, y)

    # add 'BASE' at the bottom of the axial member
    ax.text(x[0], y[0], s='BASE',
            horizontalalignment='center',
            verticalalignment='top')

    if include_loads:
        for l in mem.load_data:
            if l['location'] < 100:  # pragma: no cover
                text_x_offset = 0.001
                text_y_offset = 0
                horizontalalignment = 'left'
            else:
                text_x_offset = 0
                text_y_offset = 0.125
                horizontalalignment = 'center'

            load_loc = (l['location']/100 * mem.height)

            if l['load'].magnitude > 0:  # pragma: no cover
                plot_load_loc = load_loc + 0.25
                arrow_dy = 0.25
            else:
                plot_load_loc = load_loc + 0.50
                arrow_dy = -0.25

            ax.text(x[0] + text_x_offset, y=plot_load_loc + max(arrow_dy, 0) + text_y_offset,
                    s=f"{l['load'].magnitude} at {load_loc}",
                    horizontalalignment=horizontalalignment,
                    verticalalignment='bottom')

            ax.arrow(x[0], y=plot_load_loc, dx=0, dy=arrow_dy,
                     shape='full', width=0.0005, head_length=0.1,
                     label=l['load'].magnitude)

        plt.ylim((y[0] - 1, y[-1] + 2))

    plt.show()
