function arginfo(...args) {
    let resultObj = {};
    for (let arg of args) {
        let argType = typeof (arg);

        console.log(`${argType}: ${arg}`);
        if (!(argType in resultObj)) {
            resultObj[argType] = 0;
        }
        resultObj[argType]++
    };

    let sortedObjEntries = Object.entries(resultObj).sort((a, b) => b[1] - a[1]);

    sortedObjEntries.forEach(([key, occurence]) => console.log(`${key} = ${occurence}`))
}

// arginfo('cat', 42, function () { console.log('Hello world!'); }, function () { }, 50, 'a')