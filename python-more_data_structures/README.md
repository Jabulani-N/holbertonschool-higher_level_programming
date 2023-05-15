# Python - More Data Structures: Set, Dictionary

## Task0 - Squared simple

You can't use `copylist = examplelist.copy()` because it's a shallwo copy

- that means it'll make a copy of a list filled with references to data. the same references in the copy and original, so changing the contents of one of the lists in there changes it for both matrices.

it may be appropriate to use append to serially shove the deeper data.

### when import is allowed, import copy and use [deepcopy](https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list).