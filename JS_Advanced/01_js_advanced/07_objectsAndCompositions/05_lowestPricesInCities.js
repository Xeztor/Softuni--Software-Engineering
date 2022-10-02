function solve(infoArray) {
    let products = getAllProductsFromInput(infoArray);

    let sortedProducts = sortProducts(products);

    for (let product of Object.entries(sortedProducts)) {
        let productName = product[0]

        let lowestPriceProductObj = product[1][0]
        let productLowestPrice = lowestPriceProductObj.productPrice
        let townName = lowestPriceProductObj.townName

        console.log(`${productName} -> ${productLowestPrice} (${townName})`)
    };

    function sortProducts(productsObj) {
        for (let [_, offers] of Object.entries(productsObj)) {
            offers.sort((a, b) =>
                a.productPrice - b.productPrice || a.index - b.index
            );
            offers.sort()
        };

        return productsObj
    }

    function getAllProductsFromInput(infoArr) {
        let products = {};
        for (i = 0; i < infoArr.length; i++) {
            let [townName, productName, productPrice] = infoArr[i].split(' | ');
            productPrice = Number(productPrice);

            let productObj = {
                townName,
                productPrice,
                index: i
            };
            if (!(productName in products)) {
                products[productName] = [productObj];
                continue;
            }
            products[productName].push(productObj);
        };
        return products;
    };
}

// let test = [
//     'Sample Town | Sample Product | 1000',
//     'Sample Town | Orange | 2',
//     'Sample Town | Peach | 1',
//     'Sofia | Orange | 3',
//     'Sofia | Peach | 2',
//     'New York | Sample Product | 1000.1',
//     'New York | Burger | 10'
// ];

// solve(test)