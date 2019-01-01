import pytest
import random
from weightplotter.plotter import Plotter

def test_create_plotter():
    date_list = ["{:02}.01.19".format(x) for x in range(0, 20)]
    weight_list = [66 + random.random() for _ in range(0, 20)]
    plotter = Plotter(date_list, weight_list)
    plotter.plot()

