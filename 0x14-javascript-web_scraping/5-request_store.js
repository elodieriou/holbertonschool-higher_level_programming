#!/usr/bin/node
const fs = require('fs');
const axios = require('axios').default;

axios
  .get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  })
  .then(function () {
  });
