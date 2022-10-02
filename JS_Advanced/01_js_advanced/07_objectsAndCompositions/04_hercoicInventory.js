function heroesJSON(heroesInfoArr) {
    let heroesArr = [];
    for (let hero of heroesInfoArr) {
        let [name, level, itemsStr] = hero.split('/');
        // Trim strings and convert level to number
        name = name.trim()
        level = Number(level.trim());

        // Check if there are items
        let items = [];
        if (itemsStr) {
            items = itemsStr.trim().split(', ');
        }
        //Create hero object
        let heroObj = {
            name,
            level,
            items
        };
        // Push the object in the main array
        heroesArr.push(heroObj);
    };

    console.log(JSON.stringify(heroesArr));
}

let test1 = [
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
];
let test2 = ['Jake / 1000 /'];

heroesJSON(test1)
heroesJSON(test2)