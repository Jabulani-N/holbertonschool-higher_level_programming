#!/usr/bin/node
let Counter;
const ARGV = process.argv;
const num = parseInt(ARGV[2]);
if (ARGV[2] === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  let outputLine = '';
  for (Counter = 0; Counter < num; Counter++) {
    outputLine += 'X';
  }
  for (Counter = 0; Counter < num; Counter++) {
    console.log(outputLine);
  }
}
