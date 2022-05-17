#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
try {
  fs.writeFile(args[2], args[3], 'utf8', function (error) {
  });
}
catch(error) {
  console.log(error);
}
