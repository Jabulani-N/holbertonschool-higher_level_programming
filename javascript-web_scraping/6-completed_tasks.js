#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const length = data.length;
    const countDict = {};
    for (let i = 1; i <= 10; i++) { // loop through every userId
      let count = 0;
      for (let j = 0; j < length; j++) { // loop through every todo item
        if (data[j].userId === i && data[j].completed === true) {
          count++;
        }
      }
      if (count > 0) {
        countDict[i] = count;
      }
    }
    console.log(countDict);
  }
});
