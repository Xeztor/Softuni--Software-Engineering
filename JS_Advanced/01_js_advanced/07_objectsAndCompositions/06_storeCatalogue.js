function sortCatalogue(productsList) {
    // Sort Products
    productsList.
        sort((a, b) =>
            a.toLowerCase().localeCompare(b.toLowerCase())
        )
    // Desired format
    let products = productsList.map(product => product.replace(' :', ':'));

    // Get groups letters
    let groupLetters = new Set(products.map(product => product[0]));

    for (let letter of groupLetters) {
        console.log(letter);
        while (products.length && products[0][0].toLowerCase() == letter.toLowerCase()) {
            console.log(`  ${products.shift()}`)
        }
    };
}

// let test1 = [
//     'Appricot : 20.4',
//     'Fridge : 1500',
//     'TV : 1499',
//     'Deodorant : 10',
//     'Boiler : 300',
//     'Apple : 1.25',
//     'Anti-Bug Spray : 15',
//     'T-Shirt : 10'
// ];

// let test2 = [
//     'Banana : 2',
//     "Rubic's Cube : 5",
//     'Raspberry P : 4999',
//     'Rolex : 100000',
//     'Rollon : 10',
//     'Rali Car : 2000000',
//     'Pesho : 0.000001',
//     'Barrel : 10'
// ];

// sortCatalogue(test1);
// sortCatalogue(test2);