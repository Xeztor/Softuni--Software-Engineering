/* 
•	last() - returns the last element of the array
•	skip(n) - returns a new array which includes all original elements, except the first n elements; n is a Number parameter
•	take(n) - returns a new array containing the first n elements from the original array; n is a Number parameter
•	sum() - returns a sum of all array elements
•	average() - returns the average of all array elements
*/

(function solve() {
    Array.prototype.last = function () {
        return this[this.length - 1];
    };
    Array.prototype.skip = function (n) {
        return this.slice(n, this.length);
    };
    Array.prototype.take = function (n) {
        return this.slice(0, n);
    };
    Array.prototype.sum = function () {
        return this.reduce((acc, num) => acc + num, 0);
    };
    Array.prototype.avarege = function () {
        return this.sum() / this.length;
    };
})()

let arr = [0, 1, 2, 3, 4];
console.log(arr.last());
console.log(arr.skip(3));
console.log(arr.take(3));
console.log(arr.sum());
console.log(arr.avarege(3));