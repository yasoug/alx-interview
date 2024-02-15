#!/usr/bin/node

const request = require('request');

function pchars (chars, i) {
  if (i === chars.length) return;
  request(chars[i], function (error, response, body) {
    if (error) console.log(error);
    else {
      console.log(JSON.parse(body).name);
      pchars(chars, ++i);
    }
  });
}

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  function (error, response, body) {
    if (error) console.log(error);
    else {
      const chars = JSON.parse(body).characters;
      pchars(chars, 0);
    }
  });
