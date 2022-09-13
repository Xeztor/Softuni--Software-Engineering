function maxNumber(num1, num2, num3) {
    let maxNum = num3;
    if (num1 > num2 && num1 > num3) {
        maxNum = num1;
    } else if (num2 > num3) {
        maxNum = num2;
    } else {
        maxNum = num3;
    }

    console.log(`The largest number is ${maxNum}.`)
}
