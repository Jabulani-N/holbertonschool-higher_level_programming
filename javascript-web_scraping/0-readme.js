#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array
[javascript location (shebang), called function/file, user arguments]
*/
const fs = require('fs');
// this 'fs' seems to be shorthand for "filesystem"

fs.readFile(args[2], 'utf-8', function (error, content) {
  console.log(error || content);
}
);
// translates to fs.readFile(file_to_read, 'formatting', ???)
