const { expect, assert } = require("chai");

const chooseYourCar = require('../PaymentPackage');

describe('Choose Your Car Tests', () => {
    describe("choosingType() functionality", () => {
        it('should throw error if given year is less than 1900', () => {
            // Arrange
            let type = 'sedan';
            let color = 'red';
            let invalidYear = 1000;
            let fnToTest = () => chooseYourCar.choosingType(type, color, invalidYear);
            // Act & Assert
            assert.throws(fnToTest, `Invalid Year!`)
        });
        it('should throw error if given year is more than 2022', () => {
            // Arrange
            let type = 'sedan';
            let color = 'red';
            let invalidYear = 2030;
            let fnToTest = () => chooseYourCar.choosingType(type, color, invalidYear);
            // Act & Assert
            assert.throws(fnToTest, `Invalid Year!`)
        });
        it('should throw error if given type value is not "Sedan"', () => {
            // Arrange
            let type = 'hatchback';
            let color = 'red';
            let year = 2015;
            let fnToTest = () => chooseYourCar.choosingType(type, color, year);
            // Act & Assert
            assert.throws(fnToTest, `This type of car is not what you are looking for.`)
        });
        it('should return expected string if year is equal to 2010', () => {
            // Arrange
            let type = 'Sedan';
            let color = 'red';
            let year = 2010;
            let expectedString = `This ${color} ${type} meets the requirements, that you have.`;
            // Act
            let result = chooseYourCar.choosingType(type, color, year);
            // Assert
            expect(result).to.be.equal(expectedString);
        });
        it('should return expected string if year is more than 2010', () => {
            // Arrange
            let type = 'Sedan';
            let color = 'red';
            let year = 2015;
            let expectedString = `This ${color} ${type} meets the requirements, that you have.`;
            // Act
            let result = chooseYourCar.choosingType(type, color, year);
            // Assert
            expect(result).to.be.equal(expectedString);
        });
        it('should return expected string if year is less than 2010', () => {
            // Arrange
            let type = 'Sedan';
            let color = 'red';
            let year = 2000;
            let expectedString = `This ${type} is too old for you, especially with that ${color} color.`;
            // Act
            let result = chooseYourCar.choosingType(type, color, year);
            // Assert
            expect(result).to.be.equal(expectedString);
        });
    });
    describe("brandName functionality", () => {
        it('should throw error if argument brands is not an array', () => {
            // Arrange
            let notArrBrands = 10;
            let brandIndex = 2;
            let fnToTest = () => chooseYourCar.brandName(notArrBrands, brandIndex);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if argument brandIndex is not a number', () => {
            // Arrange
            let brands = ['BMW', 'Volkswagen', 'Renault', 'Porsche'];
            let notANumberBrandIndex = 'not a number';
            let fnToTest = () => chooseYourCar.brandName(brands, notANumberBrandIndex);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if argument brandIndex is bigger than the brands length', () => {
            // Arrange
            let brands = ['BMW', 'Volkswagen', 'Renault', 'Porsche'];
            let invalidIndexNumber = 10;
            let fnToTest = () => chooseYourCar.brandName(brands, invalidIndexNumber);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if argument brandIndex is negative integer', () => {
            // Arrange
            let brands = ['BMW', 'Volkswagen', 'Renault', 'Porsche'];
            let negativeIndexNumber = -5;
            let fnToTest = () => chooseYourCar.brandName(brands, negativeIndexNumber);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should return string of the brands array without the brand at the specific index', () => {
            // Arrange
            let brands = ['BMW', 'Volkswagen', 'Renault', 'Porsche'];
            let brandsIndex = 1;
            let expected = "BMW, Renault, Porsche"
            // Act 
            let result = chooseYourCar.brandName(brands, brandsIndex);
            // Assert
            expect(result).to.be.equal(expected)
        });
    });
    describe('carFuelConsumption() functionality', () => {
        it('should throw error if distanceInKilometers is not a number', () => {
            // Arrange
            let invalidDataType = 'not a number';
            let consumptedFuelInLiters = 2;
            let fnToTest = () => chooseYourCar.carFuelConsumption(invalidDataType, consumptedFuelInLiters);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if distanceInKilometers is a negative number', () => {
            // Arrange
            let negativeNumber = -10;
            let consumptedFuelInLiters = 2;
            let fnToTest = () => chooseYourCar.carFuelConsumption(negativeNumber, consumptedFuelInLiters);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if consumptedFuelInLiters is not a number', () => {
            // Arrange
            let distanceInKilometers = 20;
            let invalidDataType = 'not a number';
            let fnToTest = () => chooseYourCar.carFuelConsumption(distanceInKilometers, invalidDataType);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should throw error if distanceInKilometers is a negative number', () => {
            // Arrange
            let distanceInKilometers = 20;
            let negativeNumber = -2;
            let fnToTest = () => chooseYourCar.carFuelConsumption(distanceInKilometers, negativeNumber);
            // Act & Assert
            assert.throws(fnToTest, "Invalid Information!");
        });
        it('should return expected string if fuel consumption is equal to 7.00 liters', () => {
            // Arrange
            let distanceInKilometers = 100;
            let consumptedFuelInLiters = 7;
            let expectedString = `The car is efficient enough, it burns 7.00 liters/100 km.`;
            // Act
            let result = chooseYourCar.carFuelConsumption(distanceInKilometers, consumptedFuelInLiters);
            // Assert
            expect(result).to.be.equal(expectedString)
        });
        it('should return expected string if fuel consumption is less than 7.00 liters', () => {
            // Arrange
            let distanceInKilometers = 100;
            let consumptedFuelInLiters = 5;
            let expectedString = `The car is efficient enough, it burns 5.00 liters/100 km.`;
            // Act
            let result = chooseYourCar.carFuelConsumption(distanceInKilometers, consumptedFuelInLiters);
            // Assert
            expect(result).to.be.equal(expectedString)
        });
        it('should return expected string if fuel consumption is equal to 10.00 liters', () => {
            // Arrange
            let distanceInKilometers = 100;
            let consumptedFuelInLiters = 10;
            let expectedString = `The car burns too much fuel - 10.00 liters!`;
            // Act
            let result = chooseYourCar.carFuelConsumption(distanceInKilometers, consumptedFuelInLiters);
            // Assert
            expect(result).to.be.equal(expectedString)
        })
    })
})