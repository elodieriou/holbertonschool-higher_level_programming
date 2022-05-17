#!/usr/bin/node
const axios = require('axios').default;

axios
  .get(process.argv[2])
  .then(function (response) {
    const dictionary = {};
    const numberTasks = response.data.length;

    for (let i = 0; i < numberTasks; i++) {
      const completedTask = response.data[i].completed;
      const userId = response.data[i].userId;

      if (completedTask === true) {
        if (dictionary[userId] === undefined) {
          dictionary[userId] = 0;
        }
        dictionary[userId] += 1;
      }
    }
    console.log(dictionary);
  })
  .catch(function (error) {
    console.log('An error has occurred - ' + error);
  })
  .then(function () {
  });
