#!/usr/bin/node
exports.logMe = (function (item) {
  let count = -1;
  return function (item) {
    count += 1;
    console.log(count + ': ' + item);
  };
})();
