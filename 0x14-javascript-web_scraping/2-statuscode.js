#!/usr/bin/node
const axios = require('axios').default;
axios
  .get(process.argv[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  })
  .then(function () {
  });
