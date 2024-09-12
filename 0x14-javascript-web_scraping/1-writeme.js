#!/usr/bin/node

const nodefs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

nodefs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) console.log(err);
});
