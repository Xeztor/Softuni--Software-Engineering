function solve() {
    let number = document.getElementById("input").value;
    let option = document.getElementById("selectMenuTo").value;

    let result = 0;
    if (option === 'binary') {
        result = Number(number).toString(2);
    } else if (option === 'hexadecimal') {
        result = Number(number).toString(16);
    };

    let resultElement = document.getElementsByName("output")[0];
    resultElement.value = result;
}