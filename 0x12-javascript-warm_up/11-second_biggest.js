#!/usr/bin/node

const num = process.argv.length;
if (num <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);
  const topTwoNumbers = [...new Set(numbers)];
  topTwoNumbers.sort((a, b) => b - a);
  console.log(topTwoNumbers[1]);
}
