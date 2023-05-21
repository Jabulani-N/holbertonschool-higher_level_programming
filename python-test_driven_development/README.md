
# Python - Test Driven Development


This project demonstrates the use of doctest for teting python code


## Task 0

### Known Issues

is expecting error when no b value is given. should use the default value

potnetial solution:

- ensure the protootype matches request.

- remove any checks for `b is None`

- in **test** text file, ensure it expects tests with an empty b section to run normally

## Task 1

### Known Issues

does not check to ensure all lists in matrix matrix are of same length

potential solutions:

- create a list of lengths of matrix's contents, and ensure each item is the same

tests are not comprehensive