
# Python - Test Driven Development


This project demonstrates the use of doctest for teting python code.

This Readme both demonstrates the basic structure of testing via python code, and tracks progress of each project, with notes of potential pitfalls, to make learning easier for any who may reference my work.

## how to use test files:

run in the terminal:

```

python3 -m doctest -v testFile

```

optionally followed by ` | tail -4` or ` | tail -2` (on the same line) to only print final results

be sure testFile imports the module you want to test.

**import example:**

```

>>> add_integer = __import__('0-add_integer').add_integer

```

**Example of test file with a single test**

```

'comment'

>>> content that will be run as though from terminal


```

```

'Test for 0-add_integer module, within 0-add_integer.py'



'Function to test: add_integer(a, b=98)'




>>> add_integer = __import__('0-add_integer').add_integer



'test for positive integer addition'



>>> add_integer(2, 3)

5

```

5 is the expected result. The test will "fail" if running the program does not give the expected result.

If throwing an error is the expected result, the test will "pass" if running the program throws an error.

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

## Task 4

### Known Issues

does not remove masses of spaces or tabs at the beginning of new lines

potential solutions

test file has not been completed.

- outline is present
