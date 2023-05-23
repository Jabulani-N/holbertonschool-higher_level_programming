
# Python - More Classes and Objects


a pyhton directory demonstrating more class and object creation and usage

### Attributes

```

example.public_attr

example._protected_attr

example.__private_attr

```

- you can do whatever you want to a public attribute.

- you can see, but not alter, a protected attribute.

- you can't see or alter a private attribute from outside the instance.

### Potential Pitfalls

`B`e sure to capitalize your class's name.

you will have failed to document "Classname" if you instead docuemnted "classname".

## Task 5

accesses own class via instance functions

`type(self)` accesses class operations

## Task 7

### Potential Pitfalls

be sure the rectangle printer pints hte instances own `self.print_symbol` and not the class's.

the class's only exists for the purpose of altering what an instance defaults to