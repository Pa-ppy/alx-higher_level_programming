#!/usr/bin/node
const myObjectWithIncr = {
  type: 'object',
  value: 12,
  incr: function () {
    this.value++;
  }
};
console.log(myObjectWithIncr);
myObjectWithIncr.incr();
console.log(myObjectWithIncr);
myObjectWithIncr.incr();
console.log(myObjectWithIncr);
myObjectWithIncr.incr();
console.log(myObjectWithIncr);
