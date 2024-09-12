#!/usr/bin/node

const request = require('request');

const alxUrl = process.argv[2];
request(alxUrl, (err, urlResponse, body) => {
  if (err) console.error(`error: ${err}`);
  console.log(`code: ${urlResponse.statusCode}`);
});
