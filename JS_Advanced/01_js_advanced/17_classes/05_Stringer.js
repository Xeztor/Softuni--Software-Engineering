class Stringer {
    constructor(string, length) {
        this.innerString = string;
        this.innerLength = length;
    }

    increase(value) {
        if (typeof (value) !== 'number') {
            return;
        };
        this.innerLength += value;
    }

    decrease(value) {
        if (typeof (value) !== 'number') {
            return;
        };

        if (this.innerLength <= value) {
            this.innerLength = 0;
            return;
        };
        this.innerLength -= value;
    };

    toString() {
        if (this.innerLength >= this.innerString.length) {
            return this.innerString;
        };

        return (this.innerString).substring(0, this.innerLength) + '...'
    };
}

let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4);
console.log(test.toString()); // Test
