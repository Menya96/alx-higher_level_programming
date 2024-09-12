#!/usr/bin/node
const request = require('request');

const aiURL = process.argv[2];

request(aiURL, (err, res, body) => {
  if (err) console.log(err);
  const filmCount = body.split('/people/18/').length - 1;
  console.log(filmCount);
});
