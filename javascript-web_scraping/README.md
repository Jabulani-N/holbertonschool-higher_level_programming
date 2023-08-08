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

## Install all requisites at once

`curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -;sudo apt-get install -y nodejs;sudo npm install semistandard --global;sudo npm install request --global;export NODE_PATH=/usr/lib/node_modules`

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

The callback function uses the logical OR (`||`) operator to log either the value of error or content to the console.

</details>

## task2

**Be sure to install request before attempting this task.**

```
request = require('request')
request(target_url, callback_function_to_handle_errors_and_recieve_response(error, response))
```
* `error` will contain an error message: `error.message`

* `response` will contain a statusCode: `response.statsCode`

Currently, it seems that even if the item does not exist, it gives a proper 404 statusCode instead of an error. As such, I do not know what case would cause an error in this code.

## Task3

[full list of reponse attributes](https://developer.mozilla.org/en-US/docs/Web/API/Response)

[this is the database we request from](https://swapi-api.hbtn.io/documentation#vehicles
)
### Converting response (string) to object (dictionary)

when you request from the SWAPI, the body of the response you'll receive is a JSON string object. it's a perfecetly formatted dictionary, just in string form. conert it to a dictoinary.

* the interesting content from the api call will be within `response.body`

* * response has other properties, such as `reponse.statusCode`, that we do not need for this particular task.

<details>
    <summary>
    Steps I took to figure out how I'd use `response` data
    </sumamry>

```
console.log('body: ' + response.body);
console.log('type: ' + typeof response.body)
```

This gave me string, letting me know I needed to convert it to dictoinary (object)

```
const objectified = JSON.parse(response.body);
console.log('type of objectified: ' + typeof objectified)
```
I've recorded this just to have an easy potential train of thought to default to in thte future

</details>

semistandard will prefer `exampleDict.exampleAttr` over `exampleDict['exampleAttr]`

## Task4

~~each person has a films attribute, which contains a list of film objects. count the length of the list, and you have how many films a char is in.~~

we have to use  a preset url that pulls the entire films list.

1. This `response.body.results` is a list of films objects.
2. each film object has a characters attribute. that will contain a list of urls specific to a particular character.
3. we can count this by counting how many entries in that list of urls contains a link to character 18: `https://swapi-api.hbtn.io/api/people/1/`.
4. iterate through the list of film objects' character attributes, adding up to find the total.
