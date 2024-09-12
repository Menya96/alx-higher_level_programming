#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2];

request(apiURL, (err, response, body) => {
  if (err) console.error(`error: ${err}`);

  const output = {};
  const data = JSON.parse(body);

  for (let x = 0; x < data.length; x++) {
    const userId = data[x].userId;
    const complete = data[x].completed;

    if (complete && !output[userId]) output[userId] = 0;

    if (complete) output[userId]++;
  }

  console.log(output);
});
