import pytest
import random
import numpy as np
from weightplotter import util

def test_mean():
    numbers = list(range(1,11))
    mean = sum(numbers)/len(numbers)
    assert util.mean(numbers) == mean

def test_de_mean():
    numbers = list(range(1,11))
    mean = sum(numbers)/len(numbers)
    numbers_demean = [x - mean for x in numbers]
    assert util.de_mean(numbers) == numbers_demean
    
def test_ols():
    def create_random_list(size):
        return [random.random() for _ in range(0, size)]

    y = create_random_list(10)
    X = [create_random_list(10), create_random_list(10)]
    beta, yp, u = util.ols(y, X, const=True)

    assert beta is not None
    assert yp is not None
    assert type(yp) is np.ndarray
    assert u is not None
    assert type(u) is np.ndarray
