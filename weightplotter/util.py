import csv
import numpy as np

__author__ = 'Alexander Rüedlinger'
__all__ = ('mean', 'de_mean', 'ols')

from . import logger

def mean(xs):
    l = len(xs)
    mean_xs = sum(xs)/l
    return mean_xs

def de_mean(xs):
    mean_xs = mean(xs)
    return [(x - mean_xs) for x in xs]

def ols(y, X, const=True):
    """Performs an OLS regression"""

    y = np.array([y]).transpose()
    ones = np.ones(y.shape)
    X = np.array(X).transpose() 
    X = np.hstack([X, ones])
    Xp = X.transpose()
    beta = np.linalg.inv(Xp.dot(X)).dot(Xp).dot(y)
    yp = X.dot(beta)
    u = y - yp
    return beta, yp, u

def r_squared(y, u):
    """Computes the r-squared measure."""

    sq_errors = [e * e for e in u]
    sse = np.sum(sq_errors)
    tss = sum([ y * y for y in de_mean(y)])
    r_sq = 1.0 - sse / tss 
    return r_sq

def read_data(filepath):
    date_data, weight_data = [], []
    with open(filepath) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            date_key, weight_key = row.keys()
            date, weight = row[date_key], row[weight_key]
            try:
                weight_data.append(float(weight))
                date_data.append(date)
            except:
                pass

    return date_data, weight_data

