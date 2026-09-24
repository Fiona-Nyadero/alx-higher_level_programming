#!usr/bin/node
let num = parseInt(process.argv[2]);
if (isNaN(num)) {
    console.log("Missing size");
} else {
    let printLine = 'x'.repeat(num);
    for (let i = 0; i < num; i++) {
        console.log(printLine);
    }
}