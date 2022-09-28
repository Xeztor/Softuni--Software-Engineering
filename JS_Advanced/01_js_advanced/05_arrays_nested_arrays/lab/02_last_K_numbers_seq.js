function solve(n, k){
    let result = [1];
    for (i = 0; i < n - 1; i++){
        let currentArr;
        if (result.length <= k){
            currentArr = result;
        } else {
            currentArr = result.slice(result.length - k);
        }

        let currentSum = currentArr.reduce((partial_sum, a) => partial_sum + a, 0);
        result.push(currentSum);
    }
    console.log(result);
}

