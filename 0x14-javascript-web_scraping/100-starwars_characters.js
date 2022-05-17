#!/usr/bin/node
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
axios
  .get(url)
  .then(function (response) {
    const numberCharacters = response.data.characters.length;

    for (let i = 0; i < numberCharacters; i++) {
      const characters = response.data.characters[i];

      axios
        .get(characters)
        .then(function (response) {
          console.log(response.data.name);
        })
        .catch(function (error) {
          console.log('An error has occurred - ' + error);
        })
        .then(function () {
        });
    }
  })
  .catch(function (error) {
    console.log('An error has occurred - ' + error);
  })
  .then(function () {
  });
