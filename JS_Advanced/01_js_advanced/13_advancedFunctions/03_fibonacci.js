function getFibonator() {
    let nums = [0];

    return function () {
        if (nums.length == 1) {
            nums.push(1);
            return 1;
        };
        let sumLastTwo = nums.shift() + nums[0];
        nums.push(sumLastTwo);

        return sumLastTwo;
    }
}

let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13
