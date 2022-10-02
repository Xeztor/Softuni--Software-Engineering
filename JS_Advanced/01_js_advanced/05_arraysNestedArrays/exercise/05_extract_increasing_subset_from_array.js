function solve(arr){
    let biggest = 0;
    let result = [];
    for (let num of arr){
        if (num <= biggest){
            continue
        };
        biggest = num;
        result.push(num);

    };
    return result
    console.log(result);
}

solve([1, 3, 8,  4, 10, 12, 3, 2, 24])