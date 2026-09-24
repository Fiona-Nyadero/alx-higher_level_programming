#!usr/bin/node
function add(a, b) {
    let result = a + b;
    console.log(result);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));