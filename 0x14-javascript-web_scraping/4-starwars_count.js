#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;
    console.log(count);
  }
});
