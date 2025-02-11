#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    try {
      const characters = JSON.parse(body).characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.log(charError);
          } else {
            console.log(JSON.parse(charBody).name);
          }
        });
      });
    } catch (parseError) {
      console.log('Error parsing JSON:', parseError);
    }
  }
});
