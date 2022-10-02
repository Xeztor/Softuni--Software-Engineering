function townsJSON(table) {
    let resultArr = [];

    table.shift();
    for (let row of table) {
        // row = row.replaceAll('|', '');
        while (row.includes('|')) {
            row = row.replace('|', '')
        }

        let nonTrimmedValues = row.split('  ');
        let [Town, Latitude, Longitude] = nonTrimmedValues.map(x => x.trim());

        // Round numbers to 2 decimals
        [Latitude, Longitude] = [roundToTwoDecimals(Number(Latitude)), roundToTwoDecimals(Number(Longitude))];
        let cityObj = {
            Town,
            Latitude,
            Longitude
        };
        resultArr.push(cityObj);
    };

    console.log(JSON.stringify(resultArr));

    function roundToTwoDecimals(num) {
        return Math.round((num + Number.EPSILON) * 100) / 100;
    };

}

// let test1 = [
//     '| Town | Latitude | Longitude |',
//     '| Sofia | 42.696552 | 23.32601 |',
//     '| Beijing | 39.913818 | 116.363625 |'
// ];
// let test2 = [
//     '| Town | Latitude | Longitude |',
//     '| Veliko Turnovo | 43.0757 | 25.6172 |',
//     '| Monatevideo | 34.50 | 56.11 |'
// ];

// townsJSON(test1);
// townsJSON(test2);