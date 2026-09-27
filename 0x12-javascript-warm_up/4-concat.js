#!/usr/bin/node
function concat () {
  const argument1 = process.argv[2];
  const argument2 = process.argv[3];
  console.log(`${argument1} is ${argument2}`);
}

concat();
