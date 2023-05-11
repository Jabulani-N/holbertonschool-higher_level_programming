#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = ':'
    b = 'arguments'
    if len(sys.argv) == 1:
        a = '.'
    if len(sys.argv) == 2:
        b = 'argument'
    print("{:d} {:s}{:s}".format(len(sys.argv) - 1, b, a))
    for index in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(index, sys.argv[index]))
