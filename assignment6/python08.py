# Write a NumPy program to convert an data type into to a floating type.
# a2 = np.array([10, 20, 30, 40, 50], dtype='float')
# print(a2.dtype)


import numpy as np

def function1():
    a2 = np.array([10, 20, 30, 40, 50 ])
    a = a2.astype(float)

    print(a.dtype)

function1()