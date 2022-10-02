
function solve(matrix){
    let sum = sumArr(matrix[0]);
    let columns = [];

    for (i = 0; i < matrix[0].length; i++){
        let column = matrix.map((value) => value[i]);
        columns.push(column);
    };

    let allRowsCols = matrix.concat(columns);

    for (let arr of allRowsCols){
        if (sumArr(arr) !== sum){
            return console.log(false)
        };
    };

    return console.log(true)

    function sumArr(arr){
        let sum = arr.reduce((sum, a) => sum + a, 0);
        return sum
    };
}

solve([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
   )

solve([[11, 32, 45],
    [21, 0, 1],
    [21, 1, 1]])
