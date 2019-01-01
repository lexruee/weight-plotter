from . import util
from . import logger
import matplotlib.pyplot as plt
import numpy as np

class Plotter:

    def __init__(self, date_list, weight_list):
        self.weight_list = weight_list
        self.date_list = date_list
        self._plt = None

    def plot(self):
        y, X = self._prepare_data(self.weight_list, self.date_list)
        beta, yp, u = util.ols(y, X, const=True)
        a, b = beta
        logger.debug("f(x) = %s * x + %s" % (a, b))
        logger.debug("r-squared: %s " % util.r_squared(y, u))

        logger.debug("")
        logger.debug("Weight loss per day: {:2.4f} kg".format(a[0]))
        logger.debug("Weight loss per week: {:2.4f} kg".format(a[0] * 7))
        self._plt = self._create_plot(y, yp)

    def _prepare_data(self, weight_list, date_list):
        nums = list(range(0, len(weight_list)))
        X = [nums]
        y = weight_list[:]
        return y, X

    def _create_plot(self, y, yp,):
        plt.plot(range(len(y)), y, '-ob', range(len(y)), yp, '-r')
        plt.ylabel('Weight [kg]')
        plt.xlabel('Days')
        plt.ylim([63, 73])
        plt.yticks(np.arange(63, 73, 1.0))
        plt.legend(['Actual weight', 'Linear Trend (OLS)'])
        plt.grid()
        plt.title('Weight reduction and linear trend')
        return plt

    def show_plot(self):
        self._plt.show()

    def save_plot(self, output, format="png"):
        plt.savefig(output, format=format)
