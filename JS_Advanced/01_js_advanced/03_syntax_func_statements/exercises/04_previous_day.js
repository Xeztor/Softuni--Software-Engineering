function getPreviousDay(year, month, day) {
    let date = new Date(year, month, day);
    
    if (day == 1) {
        date.setDate(-1)
    } else {
        date.setDate(day - 1)
    }
    console.log(`${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`)
}

// getPreviousDay(2016, 10, 1)