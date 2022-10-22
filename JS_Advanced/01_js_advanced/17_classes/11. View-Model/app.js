class Textbox {
    constructor(selector, regex) {
        this.elements = document.querySelectorAll(selector);
        this._invalidSymbols = new RegExp(regex);
        this.value = '';
        this.attachKeystrokeEventToInputFields();
    };

    attachKeystrokeEventToInputFields() {
        for (let input of this.elements) {
            input.addEventListener('input', this.updateValueFromInputEvent.bind(this), false);
        };
    };

    get value() {
        return this._value;
    };

    set value(newVal) {
        this._value = newVal;

        this.updateInputsValues();
    };

    get elements() {
        return this._elements;
    };

    set elements(elements) {
        this._elements = elements;
    };

    isValid() {
        return this._invalidSymbols.test(this.value) ? false : true;
    }

    updateValueFromInputEvent(e) {
        this.value = e.target.value;
    }

    updateInputsValues() {
        for (let inputField of this.elements) {
            inputField.value = this.value;
        };
    };
}

let textbox = new Textbox(".textbox", /[^a-zA-Z0-9]/);
// let inputs = document.getElementsByClassName('.textbox');

// inputs.addEventListener('click', function () { console.log(textbox.value); });
