# wplot

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
