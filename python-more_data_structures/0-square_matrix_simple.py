#!/usr/bin/python3#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        noob0 = []
        noob1 = []
        for dimension1 in matrix:
            for item in dimension1:
                noob1.append(item * item)  # copy matrix[][these]
            noob0.append(noob1.copy())  # copy matrix[these][]
            noob1 = []  # reset carrier of matrix[][these]

    return noob0
