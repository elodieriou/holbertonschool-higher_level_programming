#!/usr/bin/node
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];
axios
  .get(url + episode)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log('An error has occurred. Code: ' + error.response.status);
  });
