#!/usr/bin/node
const args = process.argv;
const parseValue = parseInt(process.argv[2], 10);
let i = 0;
if (isNaN(parseValue)) {
  console.log('Missing size');
} else {
  while (i < args[2]) {
    console.log('X'.repeat(args[2]));
    i++;
  }
}
