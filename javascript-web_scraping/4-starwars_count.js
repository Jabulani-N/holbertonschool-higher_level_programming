#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/
const listOfFilms = args[2];

const request = require('request');
let timesFeatured = 0;
request.get(listOfFilms, function (error, response) {
  if (error) {
    console.log(error.message);
  } else {
    // we received the list of films
    const objectified = JSON.parse(response.body);
    // console.log(objectified.results);
    // objectiied.results is a list of film objects
    for (const filmObject of objectified.results) {
      for (const characterURL of filmObject.characters) {
        // console.log(characterURL)
        if (characterURL === 'https://swapi-api.hbtn.io/api/people/18/') {
          timesFeatured++;
        }
      }
    }
    console.log(timesFeatured.toString());
  }
}
);
