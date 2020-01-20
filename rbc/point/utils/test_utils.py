from unittest import mock

from .plot import plot_points
from ..point import Point


def test_plot_points():
    """plt.show() should be called"""
    pt = Point(3, 4, 0)

    with mock.patch('matplotlib.pyplot.show') as mock_show:
        plot_points([pt])
        mock_show.assert_called()