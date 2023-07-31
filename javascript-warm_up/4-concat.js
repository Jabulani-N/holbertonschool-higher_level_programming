#!/usr/bin/node
const args = require('process').argv;
/*
require('process').argv returns an array
[javascript location (shebang), called function/file, user arguments]
*/
if (typeof args[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(args[2]);
}
