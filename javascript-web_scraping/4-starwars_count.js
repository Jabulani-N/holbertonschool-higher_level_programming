#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/
const listOfFilms = args[2];

const request = require('request');

request.get(listOfFilms, function (error, response) {
  if (error) {
    console.log(error.message);
  } else {
    // we received the list of films
    const objectified = JSON.parse(response.body);
    console.log(objectified.results);
  }
}
);
