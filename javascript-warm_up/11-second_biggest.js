#!/usr/bin/node
let counter;
const ARGV = process.argv;
let biggest = 0;
let secondBig = 0;

if (ARGV[2] === undefined) {
  console.log(0);
} else if (ARGV[3] === undefined) {
  console.log(0);
} else {
  for (counter = 2; counter < ARGV.length; counter++) {
    if (parseInt(ARGV[counter]) > biggest) {
      biggest = parseInt(ARGV[counter]);
    }
  }
  for (counter = 2; counter < ARGV.length; counter++) {
    if (parseInt(ARGV[counter]) > secondBig && ARGV[counter] < biggest) {
      secondBig = parseInt(ARGV[counter]);
    }
  }
  console.log(secondBig);
}
