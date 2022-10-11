function attachEventsListeners() {
    let main = document.getElementsByTagName('main')[0];
    main.addEventListener('click', convert);

    const secInUnit = {
        "days": 86400,
        "hours": 3600,
        "minutes": 60,
        "seconds": 1,
    };

    function convert(event) {

        if (event.target.type !== 'button') {
            return;
        };

        let inputElements = document.querySelectorAll('div input[type="text"]');
        let givenInputElement = findFilledInput(inputElements);

        let inputInSeconds = convertInputToSeconds(givenInputElement)

        for (let inputEl of inputElements) {
            if (inputEl === givenInputElement) {
                continue;
            } else if (inputEl.id === 'seconds') {
                inputEl.value = inputInSeconds;
                continue;
            };
            let unit = inputEl.id;
            inputEl.value = inputInSeconds / secInUnit[unit];

        };
    };

    function convertInputToSeconds(inputElement) {
        let unit = inputElement.id;
        let value = inputElement.value;

        return value * secInUnit[unit];
    };

    function findFilledInput(inputElements) {
        for (let input of inputElements) {
            if (input.value) {
                return input;
            };
        };
    };
}