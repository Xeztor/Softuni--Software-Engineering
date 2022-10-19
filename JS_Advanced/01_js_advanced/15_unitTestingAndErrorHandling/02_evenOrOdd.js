const { expect } = require("chai");

function isOddOrEven(string) {
    if (typeof (string) !== 'string') {
        return undefined;
    }
    if (string.length % 2 === 0) {
        return "even";
    }

    return "odd";
}

describe("isOddOrEven", () => {

    it("passed argument is not a string returns undefined", () => {
        // Arrange
        let notAString = undefined;
        // Act
        let result = isOddOrEven(notAString)
        // Assert
        expect(result).to.be.undefined;
    });

    it("passed argument is string of odd length", () => {
        // Arrange
        let string = 'a';
        // Act
        let result = isOddOrEven(string)
        // Assert
        expect(result).to.be.equal('odd');
    });

    it("passed argument is string of even length", () => {
        // Arrange
        let string = 'ab';
        // Act
        let result = isOddOrEven(string)
        // Assert
        expect(result).to.be.equal('even');
    });

})

