#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
};
