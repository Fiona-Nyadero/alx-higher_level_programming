function printsArguments() {
    if (!process.argv[2]) {
        console.log("No argument");
    }

    let i = 2;
    while (process.argv[i] !== undefined) {
        console.log(process.argv[i]);
        i++;
    }
}

printsArguments();