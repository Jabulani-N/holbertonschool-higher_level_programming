
# Python - Almost a circle


A pyhton directory demonstrating class inheritance and unit testing

[this links to](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-examples/inheritence_notes.md) supplimentary notes taken before the project began.

## Task 0 - unittests

each task will have unittests associated with it.

[Task5 of the Test-driven Development directory of this repository](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/blob/main/python-test_driven_development/tests/6-max_integer_test.py) (tasks names are mismatched from task number, in following assigned values) demonstrates unitteset use.

there is such a thing as `assertRaises(TypeError)`

this will be graded via `python3 -m unittest discover tests`

### Potential Pitfalls

Testing getters: use `assertEqual(instance.attribute)` NOT assertEqual(instance.attribute())

### task 1 unitteset

* if given no argumenmt, self.id() should equal none

* if given a numerical arugment, self.id() should equal that value

* * negative input

* * 0 input

* * positive input


## Task 1 - Base class

take an integer argument. assign it to self.id.

[refresher](https://github.com/Jabulani-N/holbertonschool-higher_level_programming/tree/main/python-classes) of getter and setter methods:

```

    @property

    def methodname(self):

        return self.something

    @methodname.setter

    def methodname(self, some_input)

        #does something
```

## task 8 - Update

### [*args](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)

this task uses `*args`, a **tuple** that contains a variable numebr of argumemnts.

