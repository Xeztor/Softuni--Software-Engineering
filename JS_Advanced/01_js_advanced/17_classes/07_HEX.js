class Hex {
    constructor(value) {
        this.value = value;
    };

    valueOf() {
        return this.value;
    };

    toString() {
        return '0x' + String(this.value.toString(16).toUpperCase());
    };

    plus(arg) {
        let number = 0;
        if (typeof arg === 'object') {
            number = arg.value;
        };
        number = arg;

        return new Hex(this.value + number);
    };

    minus(arg) {
        let number = 0;
        if (typeof arg === 'object') {
            number = arg.value;
        };
        number = arg;

        return new Hex(this.value - number);
    };

    parse(hexNum) {
        return parseInt(hexNum, 16);
    }
}

let FF = new Hex(255);
console.log(FF.toString());
FF.valueOf() + 1 == 256;
let a = new Hex(10);
let b = new Hex(5);
console.log(a.plus(b).toString());
console.log(a.plus(b).toString() === '0xF');
console.log(FF.parse('AAA'));
