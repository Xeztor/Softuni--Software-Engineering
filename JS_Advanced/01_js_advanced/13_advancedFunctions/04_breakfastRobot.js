function solve() {
    const foodInfo = {
        apple: { carbohydrate: 1, flavour: 2 },
        lemonade: { carbohydrate: 10, flavour: 20 },
        burger: { carbohydrate: 5, fat: 7, flavour: 3 },
        eggs: { protein: 5, fat: 1, flavour: 1 },
        turkey: { protein: 10, carbohydrate: 10, fat: 10, flavour: 10 },
    };

    let ingrediantsStorage = {
        carbohydrate: 0,
        flavour: 0,
        fat: 0,
        protein: 0,
    };

    function report() {
        return `protein=${ingrediantsStorage.protein} carbohydrate=${ingrediantsStorage.carbohydrate} fat=${ingrediantsStorage.fat} flavour=${ingrediantsStorage.flavour}`;
    };

    function restock(ingrediant, qty) {
        ingrediantsStorage[ingrediant] += Number(qty);
        return 'Success';
    }

    function prepare(product, qty) {

        let productRequirements = foodInfo[product];

        for (let ingredient in productRequirements) {
            let requiredIngredient = productRequirements[ingredient] * qty
            if (requiredIngredient > ingrediantsStorage[ingredient]) {
                return `Error: not enough ${ingredient} in stock`
            };
            ingrediantsStorage[ingredient] -= requiredIngredient;
        };

        return 'Success';
    };

    return function (commandInput) {
        let [command, ...args] = commandInput.split(' ');

        switch (command) {
            case 'report': return report();
            case 'restock': return restock(...args);
            case 'prepare': ; return prepare(...args);
        }

    }
}

let manager = solve();
// console.log(manager("restock flavour 50")); // Success 
// console.log(manager("prepare lemonade 4"));
// console.log(manager('report'));


console.log(manager("restock flavour 50"));
console.log(manager("prepare lemonade 4"));
console.log(manager("restock carbohydrate 10"));
console.log(manager("restock flavour 10"));
console.log(manager("prepare apple 1"));
console.log(manager("restock fat 10"));
console.log(manager("prepare burger 1"));
console.log(manager("report"));
