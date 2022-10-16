function add(num) {
    let sum = 0;
    sum += num
    console.log(sum);
    return this
}

let a = add(1);
console.log(a);

console.log(add.call(add));
