#!/usr/bin/node
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacters () {
  axios
    .get(url)
    .then(async function (response) {
      const numberCharacters = response.data.characters.length;

      for (let i = 0; i < numberCharacters; i++) {
        const characters = response.data.characters[i];

        await axios
          .get(characters)
          .then(function (response) {
            console.log(response.data.name);
          })
          .catch(function (error) {
            console.log('An error has occurred - ' + error);
          });
      }
    })
    .catch(function (error) {
      console.log('An error has occurred - ' + error);
    });
}
getCharacters();
