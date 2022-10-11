function addItem() {
    let newItemText = document.getElementById("newItemText");
    let newItemValue = document.getElementById("newItemValue");

    let selectMenu = document.getElementById("menu");

    let newOption = document.createElement('option');
    newOption.textContent = newItemText.value;
    newOption.value = newItemValue.value;

    selectMenu.appendChild(newOption);

    clearInputs([newItemText, newItemValue])

    function clearInputs(elements) {
        for (let element of elements) {
            element.value = '';
        };
    };
}