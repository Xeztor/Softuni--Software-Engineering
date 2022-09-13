function solve(firstNum, lastNum) {
  let result = 0;
  let num1 = Number(firstNum);
  let num2 = Number(lastNum);

  for (i = num1; i <= num2; i++) {
    result += i;
  }
  console.log(result);
}

solve("1", "5");
