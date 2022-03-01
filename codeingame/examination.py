print('Hello')

from functools import reduce


def Average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


# Driver Code
lst = [64, 7556, 345, 7556, 345, 7556, 345, 7556, 433, 345, 756, 123, 942, 3112, 421, 9341, 1212, 8, 43, 41, 345, 341, 21, 321, 123]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))