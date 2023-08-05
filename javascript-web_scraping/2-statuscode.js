#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/
const urlToRequest = args[2];

const request = require('request');

request.get(urlToRequest, function (error, response) {
  if (error) {
    console.log(error.message);
  } else {
    console.log(response.statusCode);
  }
}
);
