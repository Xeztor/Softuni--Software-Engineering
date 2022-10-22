function solve(juicesInput) {
    let juices = {};

    let bottles = {};
    for (let juice of juicesInput) {
        let [juiceName, qty] = juice.split(' => ');
        qty = Number(qty);
        if (!(juiceName in juices)) {
            juices[juiceName] = 0;
        };
        juices[juiceName] += qty;
        if (juices[juiceName] >= 1000) {
            if (!(juiceName in bottles)) {
                bottles[juiceName] = 0;
            };
            bottles[juiceName] += Math.floor(juices[juiceName] / 1000);
            juices[juiceName] -= Math.floor(juices[juiceName] / 1000) * 1000;
        };
    };

    Object.entries(bottles).forEach(([fruit, bottlesQty]) => console.log(`${fruit} => ${bottlesQty}`));

}

let test1 = [
    'Orange => 2000',
    'Peach => 1432',
    'Banana => 450',
    'Peach => 600',
    'Strawberry => 549'
];

let test2 = [
    'Kiwi => 234',
    'Pear => 2345',
    'Watermelon => 3456',
    'Kiwi => 4567',
    'Pear => 5678',
    'Watermelon => 6789'
];

solve(test1);
solve(test2);