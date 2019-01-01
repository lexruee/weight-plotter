__author__ = 'Alexander Rüedlinger'
import click
from weightplotter.plotter import Plotter
from weightplotter import util
import logging

@click.command()
@click.argument('input', nargs=1)
@click.option('--output', help="Output filepath")
@click.option('--output-format', default='png', help="Output format. Default is png.")
@click.option('--debug', is_flag=True, help="Debug mode")
@click.option('--no-gui', is_flag=True, help="Don't show the gui")
def wplot(input, output, output_format, debug, no_gui):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    date_data, weight_data = util.read_data(input)
    plotter = Plotter(date_data, weight_data)
    plotter.plot()

    if not no_gui:
        plotter.show_plot()

    if output:
        plotter.save_plot(output)

if __name__ == '__main__':
    wplot()
