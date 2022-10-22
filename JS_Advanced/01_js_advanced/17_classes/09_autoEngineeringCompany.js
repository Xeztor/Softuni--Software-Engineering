function printMakesAndModelsProduction(inputStr) {
    let makes = {};
    for (let input of inputStr) {
        let [make, model, prodNums] = input.split(' | ');
        prodNums = Number(prodNums);

        if (makes.hasOwnProperty(make) === false) {
            makes[make] = {}
        };
        if (makes[make].hasOwnProperty(model) === false) {
            makes[make][model] = 0;
        };
        makes[make][model] += prodNums;
    }
    Object.entries(makes).forEach(([make, models]) => {
        console.log(make);
        Object.entries(models).forEach(([model, prodNum]) =>
            console.log(`###${model} -> ${prodNum}`)
        );
});
}

let test = [
    'Audi | Q7 | 1000',
    'Audi | Q6 | 100',
    'BMW | X5 | 1000',
    'BMW | X6 | 100',
    'Citroen | C4 | 123',
    'Volga | GAZ-24 | 1000000',
    'Lada | Niva | 1000000',
    'Lada | Jigula | 1000000',
    'Citroen | C4 | 22',
    'Citroen | C5 | 10'];

printMakesAndModelsProduction(test)