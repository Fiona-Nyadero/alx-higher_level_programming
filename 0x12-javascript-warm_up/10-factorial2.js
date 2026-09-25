#!/usr/bin/node

function factorial(n) {
    if (isNaN(n) || n === 0) {
        return 1;
    } else {
        let result = 1;
        for (i= 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}

console.log(factorial(parseInt(process.argv[2])));