function solve(commands){
    let result = [];
    let num = 0;
    for (let command of commands){
        num += 1
        if (command == 'add'){
            result.push(num);
        } else {
            result.pop()
        };
    }
    if (!result.length){
        console.log('Empty');
        return;
    };
    console.log(result.join('\n'));
}

solve(['add', 
'add', 
'add', 
'add']
)

solve(['add', 
'add', 
'remove', 
'add', 
'add'])

solve(['remove', 
'remove', 
'remove']

)
