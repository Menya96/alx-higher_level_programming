#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const starWarsURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(starWarsURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);
  const charactersArray = JSON.parse(body).characters;
  for (const xterURL of charactersArray) {
    request(xterURL, (errX, responseX, bodyX) => {
      if (errX) console.error(`error: ${errX}`);
      console.log(JSON.parse(bodyX).name);
    });
  }
});
