#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  const arr = [];
  let i = 2;
  while (i < args.length) {
    arr[i - 2] = parseInt(args[i]);
    i++;
  }
  const max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  const secondMax = Math.max.apply(null, arr);
  console.log(secondMax);
}
