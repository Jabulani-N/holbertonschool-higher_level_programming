#!/usr/bin/node
// this code is intentionally inefficnet,
//for the sake of creating examples to reference
const argv = require('process').argv;
let first = 'undefined'
let second = 'undefined'

if (typeof argv[2] != 'undefined'){
  first = argv[2];
}
if (typeof argv[3] != 'undefined'){
  second = argv[3];
}
const finalAnswer = first.concat(' is ',second )

  console.log(finalAnswer);
