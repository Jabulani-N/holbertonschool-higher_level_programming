#!/usr/bin/node

const args = require('process').argv;
/*
require('process').argv returns an array:
[javascript location (shebang), called function/file, user arguments]
*/
const fs = require('fs');
// this 'fs' is "filesystem"

const fileName = args[2];
const getsWritten = args[3];

fs.writefile(fileName, getsWritten, 'utf-8', (err) => {
  if (err) throw err;
}
);
// translates to
// fs.writeFile(file_to_write_to, content to write to file_to_write_to , 'formatting', callback arrow function that is called upon error)
