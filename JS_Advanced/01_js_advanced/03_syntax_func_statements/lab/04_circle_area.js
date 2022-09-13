function circleArea(input) {
    let inputType = typeof(input);
    if (inputType !== 'number') {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`);
        return
    }
    let r = Number(input);
    let area = Math.PI * r**2;
    console.log(area.toFixed(2));
}
