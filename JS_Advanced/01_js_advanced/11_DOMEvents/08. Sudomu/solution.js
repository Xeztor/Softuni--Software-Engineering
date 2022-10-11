function solve() {
    document.getElementsByTagName('button')[0]
        .addEventListener('click', checkBoard);

    document.getElementsByTagName('button')[1]
        .addEventListener('click', clearBoard);

    function checkBoard() {
        let tableBody = document.getElementsByTagName('tbody')[0];

        let numMatrix = Array.from(tableBody.rows).map(row => {
            return Array.from(row.children).reduce((acc, tdEl) => {
                return [...acc, tdEl.getElementsByTagName("input")[0].value];
            }, []);
        });

        let rows = numMatrix;
        let cols = numMatrix.map((_, colIndex) => numMatrix.map(row => row[colIndex]));

        let allVectors = [...rows, ...cols];
        let invalid = allVectors.filter(vector => new Set(vector).size < 3);

        let checkP = document.querySelector('#check p');
        if (invalid.length > 0) {
            document.getElementsByTagName('table')[0].style.border = '2px solid red';
            checkP.style.color = 'red';
            checkP.textContent = "NOP! You are not done yet...";
            return;
        };

        document.getElementsByTagName('table')[0].style.border = '2px solid green';
        checkP.style.color = 'green';
        checkP.textContent = "You solve it! Congratulations!";
    };

    function clearBoard() {
        let tableBody = document.getElementsByTagName('tbody')[0];
        let rows = tableBody.rows;

        for (let row of rows) {
            let cols = row.children;
            for (let col of cols) {
                inputs = col.getElementsByTagName('input');
                for (input of inputs) {
                    input.value = '';
                }
            };
        };

        document.getElementsByTagName('table')[0].style.border = '';

        let checkP = document.querySelector('#check p');
        checkP.style.color = '';
        checkP.textContent = "";
    };

};