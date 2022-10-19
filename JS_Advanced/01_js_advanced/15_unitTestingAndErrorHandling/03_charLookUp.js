const { expect } = require("chai");

function lookupChar(string, index) {
    if (typeof (string) !== 'string' || !Number.isInteger(index)) {
        return undefined;
    }
    if (string.length <= index || index < 0) {
        return "Incorrect index";
    }

    return string.charAt(index);
}

describe("lookupChar", () => {
    it("should return undefined if first argument is not a string", () => {
        // Arrange
        let notAString = undefined;
        let index = 1;
        // Act
        let result = lookupChar(notAString, index);
        //Assert
        expect(result).to.be.undefined;
    });

    it("should return undefined if first argument is not a number", () => {
        // Arrange
        let string = 'abc';
        let notAnindex = 'string';
        // Act
        let result = lookupChar(string, notAnindex);
        //Assert
        expect(result).to.be.undefined;
    });

    it("should return undefined if first argument is a floating point number", () => {
        // Arrange
        let string = 'abc';
        let index = 2.14;
        // Act
        let result = lookupChar(string, index);
        //Assert
        expect(result).to.be.undefined;
    });

    it('should return "Incorrect index" if the index is out of boundaries of the length of the string', () => {
        // Arrange
        let string = 'abc';
        let incorrectIndex = 4;
        //Act
        let result = lookupChar(string, incorrectIndex);
        // Assert
        expect(result).to.be.equal('Incorrect index');
    });

    it('should return "Incorrect index" if the index is negative number of the length of the string', () => {
        // Arrange
        let string = 'abc';
        let incorrectIndex = -1;
        //Act
        let result = lookupChar(string, incorrectIndex);
        // Assert
        expect(result).to.be.equal('Incorrect index');
    });

    it('should return character at given index of a string', () => {
        // Arrange
        let string = 'abc';
        let index = 0;
        // Act
        let result = lookupChar(string, index);
        // Assert
        expect(result).to.be.equal('a')
    })
})