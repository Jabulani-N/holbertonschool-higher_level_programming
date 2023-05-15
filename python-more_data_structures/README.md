# Python - More Data Structures: Set, Dictionary

## Task0 - Squared simple

You can't use `copylist = examplelist.copy()` because it's a shallow copy

- that means it'll make a copy of a list filled with references to data. the same references in the copy and original, so changing the contents of one of the lists in there changes it for both matrices.

it may be appropriate to use append to serially shove the deeper data.

### when import is allowed, import copy and use [deepcopy](https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list).

## Task1 - Search and replace

just reuse the code from removing the letter 'c' from before.

it uses the "translate" function

## Task2 - Unique addition

reuse code form the "find maximum" from last project. instead of storing max, *append* the  *current integer* to an array of *used_values*.`used_values.append(curent_integer)`

then, in the for loop taht iterates through the given list, do another for loop to iteraete through `used_values`, and if anything matches,turn variable `repeat` from False to True.

if, after that fro loop, `repeat` is False, then add it to `total`