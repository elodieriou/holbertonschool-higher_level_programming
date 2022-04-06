#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newDict[value] !== undefined) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
}
console.log(newDict);
