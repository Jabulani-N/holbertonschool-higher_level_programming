#!/usr/bin/python3#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        for dim1 in matrix:  # dimension 1
            dim1_size = len(dim1)
            pos = 0
            for index1 in dim1:
                if pos >= dim1_size - 1:
                    print("{:d}".format(index1))
                else:
                    print("{:d}".format(index1), end=' ')
                pos += 1
    else:
        print()
