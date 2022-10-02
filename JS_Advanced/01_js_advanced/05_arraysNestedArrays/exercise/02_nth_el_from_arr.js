function solve(arr, step){
    let filteredArr = arr.filter((a, i) => {
        if (i % step === 0){
            return a
        }
    });
    return filteredArr;
}

solve([1, 2, 3], 3)