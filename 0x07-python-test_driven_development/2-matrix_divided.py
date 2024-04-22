#!/usr/bin/python3

def matrix_divided(matrix, div):

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError
                        

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError

    if div == 0:
        raise ZeroDivisionError

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
