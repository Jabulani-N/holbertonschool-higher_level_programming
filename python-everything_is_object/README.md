# Python - Everything is object

This project will largely consist of low-context text files. Most usable information will be located within this README.

## [Python Glossary](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)

## Misc. notes

### [Aliasing by OpenBookProject](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)

`is` is different from `==`

- `is` asks if they reference the same exact object, while `==` asks if the two are of equal value.

 - - an alias `is` the original.

- - - if you want to make a clone of a list, for example, clone it via b = a[:]

each ~~varaible~~ object has an identifier: a numerical value unique to it.

if two variables point to the same object, as in `var1 is var2`, they will have the same id(entifier)

- you'll find var's identifier via `id(var)`
