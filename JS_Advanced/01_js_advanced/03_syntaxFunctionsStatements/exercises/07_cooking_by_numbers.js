'use strict';
function cook(...params){
    let functionMapper = {
        'chop': x => x /2,
        'dice': x => Math.sqrt(x),
        'spice': x => x + 1,
        'bake': x => x * 3,
        'fillet': x => x * 0.8,
    };
    let [startNum, ...operations] = params;
    
    for (let operation of operations){
        let func = functionMapper[operation];
        startNum = func(startNum);
        console.log(startNum);
    }

    
}

// cook('32', 'chop', 'chop', 'chop', 'chop', 'chop')
cook('9', 'dice', 'spice', 'chop', 'bake', 'fillet')