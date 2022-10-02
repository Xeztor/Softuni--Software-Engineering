function drawOrbit(arr){
    let [width, height, x, y] = arr;
    let matrix = Array(height).fill()
        .map(() => Array(width).fill())

    matrix[y][x] = 1;

    console.log(findLastOrbitNum(width, height, x, y))

    function findLastOrbitNum(width, height, x, y){
        let biggest = 0;
        for (let pair of [[width, x], [height, y]]){
            let [length, coordinate] = pair;

            let distanceInCurrentDimens;
            if (length / 2 >= coordinate){
                distanceInCurrentDimens = length - coordinate;
            } else {
                distanceInCurrentDimens = coordinate + 1;
            }

            if (distanceInCurrentDimens > biggest){
                biggest = distanceInCurrentDimens;
            }
        }
        return biggest
    }
    
    console.log(matrix.join('\n'))
}
// drawOrbit(5, 5, 0,0)
drawOrbit([5, 5, 2, 2])