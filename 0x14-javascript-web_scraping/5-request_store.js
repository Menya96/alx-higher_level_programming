#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const theURL = process.argv[2];
const file = process.argv[3];

request(theURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);
  const webContents = body;

  fs.writeFile(file, webContents, 'utf-8', (writeErr) => {
    if (writeErr) console.log(writeErr);
  });
});
