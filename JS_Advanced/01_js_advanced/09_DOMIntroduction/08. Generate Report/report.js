function generateReport() {
    let tableRows = Array.from(document.querySelectorAll("tbody tr"));
    let tableHeaderColumns = Array.from(document.querySelectorAll("thead tr th"));

    const columnNamesByIndex = tableHeaderColumns
        .reduce((object, column, index) => {
            return { ...object, [index]: column.textContent.trim().toLowerCase() }
        }, {});

    let columnsIndexesToGet = getColumnsIndexesToCheck(tableHeaderColumns);

    let resultArray = [];
    for (let row of tableRows) {
        let rowObj = {};
        let rowElements = Array.from(row.children);
        for (let index of columnsIndexesToGet) {
            rowObj[columnNamesByIndex[index]] = rowElements[index].textContent;
        };
        resultArray.push(rowObj);
    };

    let resultJSON = JSON.stringify(resultArray, null, 2);

    let outputArea = document.getElementById("output");
    outputArea.value = resultJSON

    function getColumnsIndexesToCheck(columns) {
        let indexes = [];

        for (let i = 0; i < columns.length; i++) {
            let checkBox = columns[i].getElementsByTagName('input')[0];
            if (!checkBox.checked) {
                continue;
            };
            indexes.push(i);
        };
        return indexes;
    };
}