#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/
const urlToRequest = 'https://swapi-api.hbtn.io/api/films/' + args[2] + '/';

const request = require('request');

request.get(urlToRequest, function (error, response) {
  if (error) {
    console.log(error.message);
  } else {
    const objectified = JSON.parse(response.body);
    console.log(objectified.title);
  }
}
);
