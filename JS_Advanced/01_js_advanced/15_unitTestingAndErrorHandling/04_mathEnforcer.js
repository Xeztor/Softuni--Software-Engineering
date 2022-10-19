const { expect, assert } = require("chai");

let mathEnforcer = {
    addFive: function (num) {
        if (typeof (num) !== 'number') {
            return undefined;
        }
        return num + 5;
    },
    subtractTen: function (num) {
        if (typeof (num) !== 'number') {
            return undefined;
        }
        return num - 10;
    },
    sum: function (num1, num2) {
        if (typeof (num1) !== 'number' || typeof (num2) !== 'number') {
            return undefined;
        }
        return num1 + num2;
    }
};

`•	addFive(num) - A function that accepts a single parameter:
o	    If the parameter is NOT a number, the function should return undefined.
o	    If the parameter is a number, add 5 to it, and return the result.

•	subtractTen(num) - A function that accepts a single parameter:
o	    If the parameter is NOT a number, the function should return undefined.
o	    If the parameter is a number, subtract 10 from it, and return the result.

•	sum(num1, num2) - A function that accepts two parameters:
o	    If any of the 2 parameters is NOT a number, the function should return undefined.
o	    If both parameters are numbers, the function should return their sum. 
`

describe('mathEnforcer', () => {
    describe("addFive", () => {
        it('should return undefinded if argument is not a number', () => {
            // Arrange
            let notANumber = undefined;
            // Act
            let result = mathEnforcer.addFive(notANumber);
            // Assert
            expect(result).to.be.undefined;
        });

        it('should return the argument number incremented with 5', () => {
            // Arrange
            let number = 1;
            // Act
            let result = mathEnforcer.addFive(number);
            // Assert
            expect(result).to.be.equal(6);
        });

        it('should return the floating point argument number incremented with 5', () => {
            // Arrange
            let number = 1.1;
            // Act
            let result = mathEnforcer.addFive(number);
            // Assert
            assert.closeTo(result, 6.1, 0.01);
        });

        it('should return the negative argument number incremented with 5', () => {
            // Arrange
            let number = -1;
            // Act
            let result = mathEnforcer.addFive(number);
            // Assert
            expect(result).to.be.equal(4);
        });
    });

    describe("subtractTen", () => {
        it('should return undefinded if argument is not a number', () => {
            // Arrange
            let notANumber = undefined;
            // Act
            let result = mathEnforcer.subtractTen(notANumber);
            // Assert
            expect(result).to.be.undefined;
        });

        it('should return the argument number with 10 subtracted from it', () => {
            // Arrange
            let number = 10;
            // Act
            let result = mathEnforcer.subtractTen(number);
            // Assert
            expect(result).to.be.equal(0);
        });

        it('should return the negative argument number with 10 subtracted from it', () => {
            // Arrange
            let number = -1;
            // Act
            let result = mathEnforcer.subtractTen(number);
            // Assert
            expect(result).to.be.equal(-11);
        });

        it('should return the floating point argument number with 10 subtracted from it', () => {
            // Arrange
            let number = 10.1;
            // Act
            let result = mathEnforcer.subtractTen(number);
            // Assert
            assert.closeTo(result, 0.1, 0.01)
        });
    });

    describe("sum", () => {
        it('should return undefinded if first argument is not a number', () => {
            // Arrange
            let notANumber = undefined;
            let number2 = 1;
            // Act
            let result = mathEnforcer.sum(notANumber, number2);
            // Assert
            expect(result).to.be.undefined;
        });

        it('should return undefinded if second argument is not a number', () => {
            // Arrange
            let notANumber = 1;
            let number2 = undefined;
            // Act
            let result = mathEnforcer.sum(notANumber, number2);
            // Assert
            expect(result).to.be.undefined;
        });

        it('should return the argument sum of the two argument numbers', () => {
            // Arrange
            let number1 = 1;
            let number2 = 1;
            // Act
            let result = mathEnforcer.sum(number1, number2);
            // Assert
            expect(result).to.be.equal(2);
        });

        it('should return the argument sum of the two negative argument numbers', () => {
            // Arrange
            let number1 = -1;
            let number2 = -1;
            // Act
            let result = mathEnforcer.sum(number1, number2);
            // Assert
            expect(result).to.be.equal(-2);
        });

        it('should return the argument sum of the two floating point argument numbers', () => {
            // Arrange
            let number1 = 1.1;
            let number2 = 1.1;
            // Act
            let result = mathEnforcer.sum(number1, number2);
            // Assert
            assert.closeTo(result, 2.2, 0.1)
        });
    });
})