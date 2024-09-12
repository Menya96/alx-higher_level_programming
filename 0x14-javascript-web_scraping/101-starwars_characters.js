#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const starWarsURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(starWarsURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);
  const xters = JSON.parse(body).characters;

  output(xters, 0);
});

function output (pips, i) {
  request(pips[i], (errP, responseP, bodyP) => {
    if (errP) console.error(`error: ${errP}`);
    console.log(JSON.parse(bodyP).name);
    if (i + 1 < pips.length) output(pips, i + 1);
  });
}
