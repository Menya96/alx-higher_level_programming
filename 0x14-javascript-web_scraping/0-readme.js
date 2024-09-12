#!/usr/bin/node

const nodefs = require('fs');

nodefs.readFile(process.argv[2], 'utf-8', (err, fileData) => {
  if (err) console.log(err);
  console.log(fileData);
});

// Future Notes for future Kelvin
// use nodejs' `fs` module to open a file
// use `process.argv` to grab the command line arguments passed in
// the first arg passed is at index argv[2]
// argv[0] is the nodejs execution path
// and argv[1] is the js file your using
