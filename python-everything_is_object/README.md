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

- noteworthily, becuase _everything_ is an object, that means that if `a = 89`, "89" is an object, and `a is 89`.

- - what _that_ means is that if `b = 89` and `a = 89`, because they both `is 89`, they actually point to the same object: `89`. `a is b`, until one of them changes.

- - - This does _not_ apply to lists, or other containers, as can be seen when one of them changes. It appears that they instead create a unique list object that contains links, likely to the same int/char/etc objects. `a = [12]`; `b = [12]`; `a is not b`

- - - - when changing the content of one of hte lists, it is equivalent to saying something like `b = 12` and then saying `b = 13`; it just makes the apppropriate new int object.

- - - - now if `l1 = [1,2]` and `l2 = l1`, l2 is the list pointed to by l1; if you make a new list, that will not affect either of them unless you tell one of them they are now pointing to the new list.