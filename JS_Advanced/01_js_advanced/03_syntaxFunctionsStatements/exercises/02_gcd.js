function gcdFinder(num1, num2) {
    let lowestNum =  num1 <= num2 ? num1 : num2;
    let divisor = lowestNum;

    while (divisor > 0) {
        if ((num1 % divisor == 0) && (num2 % divisor == 0)) {
           console.log(divisor);
           return
        }     
        divisor -= 1
    }
}

    
// gcdFinder(2154, 458)
