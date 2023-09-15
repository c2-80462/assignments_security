# Write a program that rotates the element of a list so that the element at the
# first index moves to the second index, the element in the second index moves to
# the third index, etc., and the element in the last index moves to the first index.
# Input:- [‘Sunday’,’Monday’,’Tuesday’,’Wednesday’]
# Output:- [’Wednesday’, ‘Sunday’, ’Monday’, ’Tuesday’]


input_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday']
rotated_list = [input_list[-1]] + input_list[:-1]

print(rotated_list)
