function findNeighbors(matrix){
    let result = 0;
    let prevRow = matrix[0];
    let currentRow;

    if (matrix.length == 1){
        return checkRow(matrix[0]);
    }
    for (let i = 1; i < matrix.length; i++){
        currentRow = matrix[i];
        result += neighborsMatches(prevRow, currentRow);
        prevRow = currentRow;
    };

    function neighborsMatches(row1, row2){
        let colMatches = checkCols(row1, row2);
        let rowMatches = checkRow(row1) + checkRow(row2);
        let result = colMatches + rowMatches;
        
        return result;
    };

    function checkRow(arr){
        let matches = 0;
        for (i = 1; i < arr.length; i++){
            if (arr[i] === arr[i - 1]){
                matches += 1;
            };
        };
        return matches;
    };

    function checkCols(row1, row2){
        let matches = 0;
        for (let i = 0; i < row1.length; i++){
            if (row1[i] === row2[i]){
                matches += 1;
            };
        };
        return matches;
    };
    return result;
}





let test1 = [
    ['test', 'yes', 'yo', 'ho'],
    ['well', 'done', 'yo', '6'],
    ['not', 'done', 'yet', '5']
];

let test2 = [
    ['2', '3', '4', '7', '0'],
    ['4', '0', '5', '3', '4'],
    ['2', '3', '5', '4', '2'],
    ['9', '8', '7', '5', '4']
];

let test3 = [
    [1,1,0],
    [0,1,1],
]

console.log(findNeighbors(test1));
console.log(findNeighbors(test2));
console.log(findNeighbors(test3));
