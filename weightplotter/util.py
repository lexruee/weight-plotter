import numpy as np

__author__ = 'Alexander Rüedlinger'
__all__ = ('mean', 'de_mean', 'ols')

def mean(xs):
    l = len(xs)
    mean_xs = sum(xs)/l
    return mean_xs

def de_mean(xs):
    mean_xs = mean(xs)
    return [(x - mean_xs) for x in xs]

def ols(y, X, const=True):
    y = np.array([y]).transpose()
    ones = np.ones(y.shape)
    X = np.array(X).transpose() 
    X = np.hstack([X, ones])
    Xp = X.transpose()
    beta = np.linalg.inv(Xp.dot(X)).dot(Xp).dot(y)
    yp = X.dot(beta)
    u = y - yp
    return beta, yp, u

