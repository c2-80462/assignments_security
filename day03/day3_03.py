# 3)Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3]

def function1():
    str_list = ['a', 'b', 'c', 'd', 'e']
    index_of_b = str_list.index('b')
    str_list[index_of_b] = [1, 2, 3]
    print(str_list)


function1()
