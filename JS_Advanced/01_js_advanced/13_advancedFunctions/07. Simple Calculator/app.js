function calculator() {
    function init(selector1, selector2, resultSelector) {


        function getInfoDec(fn) {
            return function () {
                num1 = Number(document.querySelector(selector1).value);
                num2 = Number(document.querySelector(selector2).value);
                resultElement = document.querySelector(resultSelector);

                return fn();
            }
        };

        function add() {
            resultElement.value = num1 + num2;
        };

        function subtract() {
            resultElement.value = num1 - num2;
        };

        let addFunc = getInfoDec(add);
        let subtractFunc = getInfoDec(subtract);

        this.add = addFunc;
        this.subtract = subtractFunc;
    };
    return { init };

}

const calculate = calculator();
calculate.init('#num1', '#num2', '#result');
