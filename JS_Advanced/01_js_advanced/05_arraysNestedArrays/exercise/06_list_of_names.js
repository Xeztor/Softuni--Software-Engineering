function solve(names){
   names
   .sort((a, b) => a.localeCompare(b))
   .forEach((element, index) => console.log(`${index + 1}.${element}`))
}