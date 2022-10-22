const { expect, assert } = require("chai");

const PaymentPackage = require('../PaymentPackage');

// Should throw an error

describe('Initate Object', () => {
    describe('Invalid name property initalization', () => {
        it('should throw Err if name is not string', () => {
            // Arrange
            let notAString = [];
            let number = 1
            let creationFn = () => new PaymentPackage(notAString, number);
            // Act and Assert
            assert.throws(creationFn, "Name must be a non-empty string")
        });

        it('should throw Err if name is empty string', () => {
            // Arrange
            let notAString = "";
            let number = 1
            let creationFn = () => new PaymentPackage(notAString, number);
            // Act and Assert
            assert.throws(creationFn, "Name must be a non-empty string")
        });
    });


    describe('Invalid value property initalization', () => {
        it('should throw Err if number is not a number', () => {
            // Arrange
            let string = 'SomePackage';
            let notANumber = [];
            let creationFn = () => new PaymentPackage(string, notANumber);
            // Act and Assert
            assert.throws(creationFn, "Value must be a non-negative number")
        });

        it('should throw Err if number is a negative number', () => {
            // Arrange
            let string = 'SomePackage';
            let negativeNumber = -1;
            let creationFn = () => new PaymentPackage(string, negativeNumber);
            // Act and Assert
            assert.throws(creationFn, "Value must be a non-negative number")
        });
    });

    describe('Valid object initialization', () => {
        it('should create object with name "Some Package" and value of 5', () => {
            // Arrange
            let string = 'Some Package';
            let number = 5;
            // Act
            let package = new PaymentPackage(string, number);
            // Assert
            expect(package).to.have.property("name", 'Some Package');
            expect(package).to.have.property("value", 5);
        });
    });
});

describe('Object properties of valid initialization', () => {
    describe('property VAT', () => {
        describe('default value', () => {
            it('should return 20', () => {
                // Arrange
                let string = 'Some Package';
                let number = 5;
                // Act
                let package = new PaymentPackage(string, number);
                // Assert
                expect(package).to.have.property("VAT", 20);
            })
        });
        describe('setter', () => {
            // it('should throw if try to set VAT to non number data type', () => {
            //     // Arrange
            //     let string = 'Some Package';
            //     let number = 5;
            //     let package = new PaymentPackage(string, number);
            //     let fnToTest = () => package.VAT = [];

            //     // Act & Assert
            //     assert(fnToTest, "VAT must be a non-negative number");
            // });

            // it('should throw if try to set VAT to negative number', () => {
            //     // Arrange
            //     let string = 'Some Package';
            //     let number = 5;
            //     let package = new PaymentPackage(string, number);
            //     let fnToTest = () => package.VAT = -1;
            //     // Act & Assert
            //     assert(fnToTest, "VAT must be a non-negative number");
            // });

            // it('should set VAT to 10', () => {
            //     // Arrange
            //     let string = 'Some Package';
            //     let number = 5;
            //     let package = new PaymentPackage(string, number);
            //     // Act
            //     package.VAT = 10;
            //     // Assert
            //     expect(package).to.have.property("VAT", 10);
            // });
        });
    });

    describe('property active', () => {
        it('should have default value of true', () => {
            // Arrange
            let string = 'Some Package';
            let number = 5;
            // Act
            let package = new PaymentPackage(string, number);
            // Assert
            expect(package).to.have.property("active", true);
        });

        it('should throw error if try to set with non boolean value', () => {
            // Arrange
            let string = 'Some Package';
            let number = 5;
            let package = new PaymentPackage(string, number);
            let fnToTest = () => package.active = [];
            // Act & Assert 
            assert.throws(fnToTest, "Active status must be a boolean");
        });
    });
    describe('method toString()', () => {
        it('should return string without label (inactive) if package is active (true)', () => {
            // Arrange
            let string = 'Some Package';
            let number = 5;
            let package = new PaymentPackage(string, number);
            // Act
            let output = package.toString()
            // Assert
            let expectedOutput = [
                `Package: ${package.name}` + (package.active === false ? ' (inactive)' : '') + '\n',
                `- Value (excl. VAT): ${package.value}\n`,
                `- Value (VAT ${package.VAT}%): ${package.value * (1 + package.VAT / 100)}`
            ];
            expect(output).to.be.equal(expectedOutput.join(''))
        });

        it('should return string with label (inactive) if package is not active (false)', () => {
            // Arrange
            let string = 'Some Package';
            let number = 5;
            let package = new PaymentPackage(string, number);
            package.active = false;
            // Act
            let output = package.toString()
            // Assert
            let expectedOutput = [
                `Package: ${package.name}` + (package.active === false ? ' (inactive)' : '') + '\n',
                `- Value (excl. VAT): ${package.value}\n`,
                `- Value (VAT ${package.VAT}%): ${package.value * (1 + package.VAT / 100)}`
            ];
            expect(output).to.be.equal(expectedOutput.join(''))
        });
    });
})
