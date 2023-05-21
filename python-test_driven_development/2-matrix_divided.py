#!/usr/bin/python3
"""moldule 2-matrix_divided

there is no module 1-...

this module divides all elements of a matrix matrix by div
"""


def matrix_divided(matrix, div):
    """ensures input is matrix and divisor

    ensures divisor is not 0
    divides matrix elements and returns result
    does not cnahge input matrix itself
    """

    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for checker in matrix:
        if isinstance(checker, list) is False:
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
        for item in checker:
            if isinstance(item, int) is False and \
               isinstance(item, float) is False:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            # all matrix/div instances below this point are valid
            divided_matrix = []
            item_copy = []
    for row in matrix:
        for column in row:
            item_copy.append(round(column/div, 2))
        divided_matrix.append(item_copy)
        item_copy = []

    return divided_matrix
