import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

data = np.loadtxt('input')
def count_increments(x):
    return np.sum(x > np.insert(x, 0, np.inf)[:-1])

answer1 = count_increments(data)

data_part2 = np.sum(sliding_window_view(data, 3), axis=1)

answer2 = count_increments(data_part2)

print(answer1, answer2)
