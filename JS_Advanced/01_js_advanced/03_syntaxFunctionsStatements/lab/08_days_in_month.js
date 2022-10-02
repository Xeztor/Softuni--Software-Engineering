function getDaysInMonth(month, year) {
    let date = new Date(year, month, 0);
    let days = date.getDate();
    console.log(days);
}

// getDaysInMonth(12, 2021)

