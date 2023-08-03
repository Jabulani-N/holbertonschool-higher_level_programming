# JavaScript - Web scraping

## Resources


* [working with json data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

* [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)

* [Request Module](https://github.com/request/request)

* [Modern JavaScript Cheatsheet](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)

## Install Node 10

1. `curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -`

2. `sudo apt-get install -y nodejs`

## Install Semistandard

* `sudo npm install semistandard --global`

## Install `request` module and use it

1. `sudo npm install request --global`

2. `export NODE_PATH=/usr/lib/node_modules`


## Task0

[readfile](https://nodejs.org/api/fs.html#filehandlereadfileoptions)

[more advanced readfile that utilizes a filepicker window](https://developer.mozilla.org/en-US/docs/Web/API/FileSystemFileHandle)

Write a script that reads and prints the content of a file.

* The first argument is the file path

* The content of the file must be read in utf-8

* If an error occurred during the reading, print the error object