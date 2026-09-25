#!/usr/bin/node

let num = process.argv.length;
if (num <= 3) {
    console.log(0);
} else {
    let numbers = process.argv.slice(2).map(Number);
    let topTwoNumbers = [...new Set(numbers)];
    topTwoNumbers.sort((a, b) => b - a);
    console.log(topTwoNumbers[1]);
}