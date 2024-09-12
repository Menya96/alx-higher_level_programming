#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const starWarsURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(starWarsURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);
  console.log(JSON.parse(body).title);
});
