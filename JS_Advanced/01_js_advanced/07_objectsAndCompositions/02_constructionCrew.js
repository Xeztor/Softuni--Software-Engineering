function hydrate(worker) {
    if (worker.dizziness === true) {
        worker.levelOfHydrated += 0.1 * worker.weight * worker.experience;
        worker.dizziness === false
    };

    return worker;
}

// let test1 = {
//     weight: 80,
//     experience: 1,
//     levelOfHydrated: 0,
//     dizziness: true
// };

// let test2 = {
//     weight: 120,
//     experience: 20,
//     levelOfHydrated: 200,
//     dizziness: true
// };

// let test3 = {
//     weight: 95,
//     experience: 3,
//     levelOfHydrated: 0,
//     dizziness: false
// };

// console.log(hydrate(test1))
// console.log(hydrate(test2))
// console.log(hydrate(test3))