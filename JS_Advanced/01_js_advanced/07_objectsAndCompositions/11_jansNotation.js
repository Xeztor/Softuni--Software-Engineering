function solve(arr) {
    const operations = {
        '-': (a, b) => a - b,
        '+': (a, b) => a + b,
        '/': (a, b) => a / b,
        '*': (a, b) => a * b
    };
    // Find operator index
    let index = 0;
    while (typeof arr[index] == 'number') {
        index++;
    };
    let operators = arr.slice(index);
    // Cut array
    arr.splice(index);
    let numbers = arr;

    if (operators.length > numbers.length - 1) {
        console.log("Error: not enough operands!");
        return;
    } else if (operators.length < numbers.length - 1) {
        console.log("Error: too many operands!");
        return;
    }

    for (let operator of operators) {
        let [num2, num1] = [numbers.pop(), numbers.pop()];

        let func = operations[operator];
        let result = func(num1, num2);
        numbers.push(result);
    };
    console.log(numbers[0]);
}

solve([3, '-']);
solve([5, 3, 4, '*', '-']);