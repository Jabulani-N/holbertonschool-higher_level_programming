
# Python - Inheritance

A pyhton directory demonstrating class inheritance

[this links to](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-examples/inheritence_notes.md) supplimentary notes taken before the project began.

## Task 0 - lookup

`dir(obj)` returns a list of all attributes and methods available to `obj`.

`list(stuff)` converts serially create items, such as from `x for x in range(y)` statements, into a list and returns the created list. if given a list, returns a copy of the same list given. `list(ex_list)` **does not** returns an alias of ex_list.

```

>>> list(x for x in range(4))

[0, 1, 2, 3]

>>>

```
## Task 1 - My list

`sorted(ex_list)` returns a list containing ex_list's elements, but sorted alphanumerically.

you can do `ex_MyList = MyList()` to initialize a MyList.

### how to use test files:

run in the terminal:

```

python3 -m doctest -v testFile

```

optionally followed by ` | tail -4` or ` | tail -2` (on the same line) to only print final results

be sure testFile imports the module you want to test.

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

## Task 2

`isinstance(exam, a_class)` will say True if the exam is a child inherited from a_class.
