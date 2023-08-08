#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const inputURL = process.argv[2];
const path = process.argv[3];

request(inputURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
