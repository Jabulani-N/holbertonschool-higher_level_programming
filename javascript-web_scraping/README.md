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


## Task0,1

[readfile](https://nodejs.org/api/fs.html#filehandlereadfileoptions)

[writefile with callback](https://nodejs.org/api/fs.html#fswritefilefile-data-options-callback)

* this one shows that you are expected/permitted to provide a funciton that runs when reveiving an error.

[more advanced readfile that utilizes a filepicker window](https://developer.mozilla.org/en-US/docs/Web/API/FileSystemFileHandle)

Write a script that reads and prints the content of a file.

* The first argument is the file path

* The content of the file must be read in utf-8

* If an error occurred during the reading, print the error object


<details>
    <summary>
        Explanation of my readFile line in task0, according to you.com
    </summary>

The readFile() method uses a callback function to handle the results of the file read operation. This callback function takes two arguments: error and content.

If an error occurs during the read operation, the error parameter will contain information about the error. If no error occurs, the content parameter will contain the contents of the file.

The callback function uses the logical OR (||) operator to log either the value of error or content to the console.

</details>

## task2

Be sure to install request before attempting this task.

```

request = require('request')

request(target_url, callback_function_to_handle_errors_and_recieve_response(error, response))

```
* `error` will contain an error message: `error.message`

* `response` will contain a statusCode: `response.statsCode`