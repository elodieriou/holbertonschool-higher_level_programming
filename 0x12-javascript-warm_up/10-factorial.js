#!/usr/bin/node
function factorial (x) {
  const nb = parseInt(x);
  if (isNaN(nb) || x === 0) {
    return 1;
  } else {
    return x * factorial(nb - 1);
  }
}
console.log(factorial(parseInt(process.argv[2], 10)));
