#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/

const request = require('request')
const urlToRequest = args[2];

request(urlToRequest, function (error, response) {
  console.log(error || 'code: ' + response);
}
);
// translates to
// fs.writeFile(file_to_write_to, content to write to file_to_write_to , 'formatting', callback arrow function that is called upon error)
