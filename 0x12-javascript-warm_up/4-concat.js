#!/usr/bin/node
function concat() {
    let argument1 = process.argv[2];
    let argument2 = process.argv[3];
    console.log(`${argument1} is ${argument2}`);
}

concat();