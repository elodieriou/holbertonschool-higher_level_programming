#!/usr/bin/node
const args = process.argv;
const parseValue = parseInt(args[2], 10);
if (isNaN(parseValue)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseValue);
}
