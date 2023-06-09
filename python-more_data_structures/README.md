# Python - More Data Structures: Set, Dictionary

`type([])` == list

`type({})` == dict [dictionary]

`type(set())` == set


## Task0 - Squared simple

You can't use `copylist = examplelist.copy()` because it's a shallow copy

- that means it'll make a copy of a list filled with references to data. the same references in the copy and original, so changing the contents of one of the lists in there changes it for both matrices.

it may be appropriate to use append to serially shove the deeper data.

### when import is allowed, import copy and use [deepcopy](https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list).

## Task1 - Search and replace

just reuse the code from removing the letter 'c' from before.

it uses the "translate" function

translate requires a string, and we are given int.

- easiest thing is to just check if each on matches the search and if so append replace.

- - alternative (way more code) is to convert current item to string, and translate *that* into the stirng for replace, and then convert the newly created value back into int.

- "if equal" approach also prevents issues where searching for 2 replaces 22 with "replacereplace"
## Task2 - Unique addition

turns out it means it just wants to add every single value, but only add each value once, so the approach below goes too far.

*append* the  *current integer* to an array of *used_values*.`used_values.append(curent_integer)`

then loop through again

if current value is in `used_values`,  then `repeat.append(current_value)`

loop once more

if currernt value is not in `repeat` `total += current_value`

## Task3 - Present in both


~~for item1 in first_array, for item2 in second_array, if item1 == item2, it is in both.~~

they're sets, not lists. different operations will be used.

just do the [set comprhension](https://docs.python.org/3/tutorial/datastructures.html#sets). Reading the instructions is life-changing.

### potential pitfall: set

empty sets are created via `set(setname)`

empty dictionaries are created via `dictname = {}`

this is relevant for `isinstance()` as they return different results for `type()`

## Task6 - Print sorted dictionary

`sorted(dictname)` returns a list of dictname's keys alphabetically

- when used on listname, it returns a list of listname's contents alphabetically

## Task 7 - Update

### This task will not pass the holberton checker unless your Task6 in the same repository does as well.

`setname.update(othersetname)` adds contents of othersetname to setname.

- also works on dicts.

- - when used on dicts, it replaces any already present definitions in setname with waht othersetname says.

## Task 8 - Simple Delete

### This task will not pass the holberton checker unless your Task6 in the same repository does as well.

`dictname.pop(key, returnsThisIfKeyNotFound)`

## Task 10 -

uses `max(dictname.valeus())`, which returns the highest value within dictname.

- you'll have to find which dictname[keyname] == the returned value.