#!/usr/bin/node
function callMeMoby(x, theFunction) {
    if (x <= 0) {
        console.log('Please provide a valid/positive number');
    } else {
        for (let i = 0; i < x; i++) {
            theFunction();
        }
    }
}

module.exports.callMeMoby = callMeMoby;