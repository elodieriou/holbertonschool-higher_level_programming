#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const dataFileA = fs.readFileSync(args[2], 'utf8');
const dataFileB = fs.readFileSync(args[3], 'utf8');
const content = dataFileA + dataFileB;
fs.writeFile(args[4], content, err => {
  if (err) {
    console.error(err);
  }
});
