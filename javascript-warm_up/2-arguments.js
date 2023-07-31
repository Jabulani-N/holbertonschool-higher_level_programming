#!/usr/bin/node
const args = require('process').argv;
/*
require('process').argv returns an array
[javascript location (shebang), called function/file, user arguments]
*/
if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
