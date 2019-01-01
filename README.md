# wplot

A helper program to plot weight measurements and the linerar trend based on the data.
The input file must be in the `csv` format. First column must be the `date` values, 
while the second column must contain the `weight` measurements.

## Installation

```
git clone https://github.com/lexruee/weight-plotter
cd weight-plotter
pipenv --three
pipenv install -e .
```

## Usage
```
pipenv run wplot --help
```

```
Usage: wplot [OPTIONS] INPUT

Options:
  --output TEXT         Output filepath
  --output-format TEXT  Output format. Default is png.
  --debug               Debug mode
  --no-gui              Don't show the gui
  --help                Show this message and exit.
```

## Example Usage

```
pipenv run wplot tests/data.csv 
```

![](https://raw.githubusercontent.com/lexruee/weight-plotter/master/figure.png)
