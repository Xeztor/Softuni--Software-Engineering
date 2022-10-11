function solve() {
    let binaryOption = document.createElement('option');
    binaryOption.textContent = "Binary";
    binaryOption.setAttribute("value", "binary");
    let hexdecOption = document.createElement('option');
    hexdecOption.textContent = "Hexadecimal";
    hexdecOption.setAttribute("value", "hexadecimal");

    let selectMenuTo = document.getElementById("selectMenuTo");
    selectMenuTo.appendChild(binaryOption);
    selectMenuTo.appendChild(hexdecOption);


    document.getElementsByTagName("button")[0]
        .addEventListener('click', convert);

    function convert() {
        let result = 0;
        let number = document.getElementById("input").value;
        let option = selectMenuTo.value;
        if (option === 'binary') {
            result = Number(number).toString(2);
        } else if (option === 'hexadecimal') {
            result = Number(number).toString(16).toLocaleUpperCase();
        };

        let resultElement = document.getElementsByName("output")[0];
        resultElement.value = result;
    }

}