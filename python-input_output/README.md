
# Python - Input/Output

Directory about file reading in Python, and input/output operations.

## Task 0,1,2 - Read from file, Write to file, append to file

[summary of reading and writing, among other functions](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

writing to file uses the following syntax: `f.write(string)` where f has been made equal to an opened file., and string is what you want to write to the file.

to read and write a file, one must use r+. rw does not work. 'a' opens the file for appending.

- when a file is opened for appending, uwsing write will append to the file instead of overwriting it.

## Task 3,4,5,6 - JSON

`import json`

[article](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json)

terms

* serilization: converting an object into string representation

* deserilisation: converting the JSON string representation into a python object

you can turn a python object into json via `json.dumps(ex_object)`, which will return it, or `json.dump(x, f)`, which serializes object x into text file f.

to turn an item back again from file f which ahs been opened for reading, use `x = json.load(f)`.

- similarly to dump and dumps, `json.loads(obj)`,performs the operation with oython objects instaed.

using `with` to open files causes it to automatically close the file. you can see this via `example_file_object.closed()`, which will return `True` or `False` based on current status.