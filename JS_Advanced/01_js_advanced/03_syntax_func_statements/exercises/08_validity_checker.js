function validityChecker(x1, y1, x2, y2){
    let center = [0, 0];
    let point1 = [x1, y1];
    let point2 = [x2, y2];

    let pointsPairs = [
        [center, point1],
        [center, point2],
        [point2, point1],
    ]

    for (i = 0; i < 3; i++){
        let points_to_check = pointsPairs[i];
        let pointsString = `{${points_to_check[1][0]}, ${points_to_check[1][1]}} to {${points_to_check[0][0]}, ${points_to_check[0][1]}}`;

        if (!checkDistanceValid(points_to_check)){
            console.log(`${pointsString} is invalid`);
            continue
        }

        console.log(`${pointsString} is valid`);
    }
    function checkDistanceValid(points){
        let [x1, y1] = points[0];
        let [x2, y2] = points[1];

        let distance = Math.sqrt((x2-x1)**2 + (y2-y1)**2);
        if (isNaN(distance) || !Number.isInteger(distance) || distance < 0){
            return false;
        }

        return true;
    }    
}


// validityChecker(2, 1, 1, 1)