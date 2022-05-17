#!/usr/bin/node
const axios = require('axios').default;
axios
  .get(process.argv[2])
  .then(function (response) {
    let count = 0;
    const numberFilm = response.data.results.length;
    for (let i = 0; i < numberFilm; i++) {
      for (let j = 0; j < response.data.results[i].characters.length; j++) {
        if (response.data.results[i].characters[j].includes('18') === true) {
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
