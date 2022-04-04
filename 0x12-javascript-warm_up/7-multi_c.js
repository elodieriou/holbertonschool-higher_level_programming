#!/usr/bin/node
const args = process.argv;
const parseValue = parseInt(process.argv[2], 10);
let i = 0;
if (isNaN(parseValue)) {
  console.log('Missing number of occurrences');
} else {
  while (i < args[2]) {
    console.log('C is fun');
    i++;
  }
}
