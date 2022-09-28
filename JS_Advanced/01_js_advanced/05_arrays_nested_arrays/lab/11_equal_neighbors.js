function findNeighbors(matrix){
    let result = 0;
    let prevRow = matrix[0];
    let currentRow;

    for (let i = 1; i < matrix.length; i++){
        currentRow = matrix[i];
        result += neighborsMatches(prevRow, currentRow);
        prevRow = currentRow;
    };

    function neighborsMatches(row1, row2){
        let result = 0;
        for (let i = 0; i < row1.length; i++){
            if (row1[i] === row2[i] || row1[i] === row1[i + 1] || row2[i] === row2[i + 1]){
                result += 1;
            };
        };
        return result;
    };

    return result;
    
}





// let test1 = 
// [['test', 'yes', 'yo', 'ho'],
// ['well', 'done', 'yo', '6'],
// ['not', 'done', 'yet', '5']];

// let test2 = 
// [['2', '3', '4', '7', '0'],
// ['4', '0', '5', '3', '4'],
// ['2', '3', '5', '4', '2'],
// ['9', '8', '7', '5', '4']];

// console.log(findNeighbors(test1));
// console.log(findNeighbors(test2));
