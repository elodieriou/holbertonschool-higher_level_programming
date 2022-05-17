#!/usr/bin/node
const axios = require('axios').default;
axios
  .get(process.argv[2])
  .then(function (response) {
    let count = 0;
    const numberFilm = response.data.results.length;

    for (let i = 0; i < numberFilm; i++) {
      const numberCharacters = response.data.results[i].characters.length;

      for (let j = 0; j < numberCharacters; j++) {
        const filmForCharacter = response.data.results[i].characters[j];

        if (filmForCharacter.includes('18') === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log('An error has occurred - ' + error);
  })
  .then(function () {
  });
