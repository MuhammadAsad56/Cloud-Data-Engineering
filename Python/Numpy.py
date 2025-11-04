import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

# print(np_height.ndim)

# 2d numpy

np_2d = np.array( [ [1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, 68.7] ] )

# np_2d_height = np_2d[0]
# np_2d_weight = np_2d[1]

# print(np_2d[:, 1])


np_city = np.array([[1.64, 71.78],[1.37, 63.35], [1.76, 55.09],[2.04, 74.85],[2.04, 68.72],[2.01, 73.57],
                   [2.64, 73.78],[3.37, 65.35], [4.76, 65.09],[5.04, 76.85],[6.04, 68.72],[7.01, 73.67],
                   [1.64, 71.78],[1.37, 63.35], [1.76, 55.09],[2.04, 74.85],[2.04, 68.72],[2.01, 73.57]])

# print(np_city[:, 0])


# print(np_city.shape)   # 18 Rows , 2 columns
# result (18, 2)


# height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
# weight = np.round(np.random.normal(60.32, 15, 5000), 2)

# print(height[0])


# where method
# np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
# print(np.where(np_weight < 70 , np_weight , 2))
# result [65.4 59.2 63.6  2.  68.7]

# arr = np.array([5, 10, 15, 20, 25, 30])
# arr = (arr > 10 ) & (arr < 30)
# print(arr)
# fiter_arr = arr[mask]
# print(fiter_arr)

# TASK:

# use np.where() to filter tyhe data form weight or height array
# Given a 2D NumPy array, write a function to set the elements on the main diagonal to zero without affecting other elements.
# Given a 1D NumPy array, write a function to return the indices of the top-k largest elements.

# weight_height = np.array([[40.5, 45.6, 55.8, 60.2],[5, 5.3, 6.3,7 ]])

# print(weight_height[:, 1:3])

# np.where()

# arr = np.array([[1,2,3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# np.fill_diagonal(arr, 0)
# print(arr)


