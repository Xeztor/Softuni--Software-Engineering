function checkNumbersSame(numbers) {
    let numsString = String(numbers);
    let sumOfNums = sum(numsString)
    

    for (i = 0; i < numsString.length; i++) {
        if (numsString[i] != numsString[0]) {
            console.log(false);
            console.log(sumOfNums);
            return
        }
    }   
    console.log(true);
    console.log(sumOfNums);

    function sum(numbers){
        let result = 0;
        for (i = 0; i < numbers.length; i++) {
            result += Number(numbers[i]);
        }
        return result;
    }

}



// checkNumbersSame(2222222)
// checkNumbersSame(1234)
