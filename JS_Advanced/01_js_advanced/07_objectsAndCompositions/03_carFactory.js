function carFactory(requirements) {
    let car = {
        model: requirements.model,
    };
    const carEngines = {
        smallEngine: { power: 90, volume: 1800 },
        normalEngine: { power: 120, volume: 2400 },
        monsterEngine: { power: 200, volume: 3500 },
    };

    const carriages = {
        hatchback: { type: 'hatchback', color: undefined },
        coupe: { type: 'coupe', color: undefined },

    };

    if (requirements.power <= 90) {
        car.engine = carEngines.smallEngine;
    } else if (requirements.power <= 120) {
        car.engine = carEngines.normalEngine;
    } else {
        car.engine = carEngines.monsterEngine;
    }

    car.carriage = { ...carriages[requirements.carriage] };
    car.carriage.color = requirements.color;

    let wheelsize = requirements.wheelsize
    if (requirements.wheelsize % 2 === 0) {
        wheelsize--;
    }
    car.wheels = Array(4).fill(wheelsize)

    return car
}

// let test1 = {
//     model: 'VW Golf II',
//     power: 90,
//     color: 'blue',
//     carriage: 'hatchback',
//     wheelsize: 14
// }
//     ;
// let test2 = {
//     model: 'Opel Vectra',
//     power: 110,
//     color: 'grey',
//     carriage: 'coupe',
//     wheelsize: 17
// }
//     ;

// console.log(carFactory(test1));
// console.log(carFactory(test2));

//{
//  model: <model name>,
//  power: <minimum power>,
//  color: <color>,
//  carriage: <carriage type>,
//  wheelsize: <size>
//};
