"use-strict";
function ticTacToe(moves){
    let board = [
        [false, false, false],
        [false, false, false],
        [false, false, false],
    ];

    let char = 'X';

    let winner;
    for (let i = 0; i < moves.length; i++){
        let [y, x] = moves[i].split(' ');
        [x, y] = [Number(x), Number(y)];
        if (board[y][x] !== false){
          console.log("This place is already taken. Please choose another!")
          continue
        };

        board[y][x] = char;
        char = changeChar(char);

        winner = checkBoard(board);
        if (winner){
            console.log(`Player ${winner} wins!`);
            break
        };

        if (!board.flat().includes(false)){
            console.log("The game ended! Nobody wins :(");
            break
        };
    };

    board.forEach(row => console.log(row.join('\t')))

    function checkBoard(board){
        let rows = board.slice();
        
        // Create diagonals arrays
        let mainDiagonal = rows.map((row, index) => row[index]);
        let seconadryDiagonal = rows.map((row, index) => row[row.length - index - 1]);

        // Create columns arrays
        let cols = [];
        for (let i = 0; i < 3; i++){
            let col = rows.map(row => row[i]);
            cols.push(col);
        };

        // Merge all arrays to check for winner
        let allChecks = [...rows, ...cols, mainDiagonal, seconadryDiagonal];

        let winner;
        for (let arr of allChecks){
            let setOfCheck = new Set(arr);
            if (setOfCheck.size == 1 && !setOfCheck.has(false)){
                [winner] = setOfCheck;
                return winner;
            };
        };

        // Return 0 if no winner is found
        return 0;
    };

    function changeChar(previousPlayerChar){
        if (previousPlayerChar == 'O'){
            return 'X';
        };
        return 'O';
    };
};
// let test1 = ["0 1",
// "0 0",
// "0 2", 
// "2 0",
// "1 0",
// "1 1",
// "1 2",
// "2 2",
// "2 1",];

// let test2 = ["0 0",
// "0 0",
// "1 1",
// "0 1",
// "1 2",
// "0 2",
// "2 2",
// "1 2",
// "2 2",
// "2 1"]; 

let test3 = ["0 1",
"0 0",
"0 2",
"2 0",
"1 0",
"1 2",
"1 1",
"2 1",
"2 2",
"0 0"]

// ticTacToe(test1)
// ticTacToe(test2)
ticTacToe(test3)
