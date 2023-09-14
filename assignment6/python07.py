#  Write a NumPy program to create an array with the values 1, 7, 13, 105 and
# determine the size of the memory occupied by the array


import numpy as np


def function1():
    np_array = np.array([1, 17, 13, 105])
    print(f"The array is {np_array}")
    print(f"The array occupies {np_array.nbytes} bytes")


function1()
