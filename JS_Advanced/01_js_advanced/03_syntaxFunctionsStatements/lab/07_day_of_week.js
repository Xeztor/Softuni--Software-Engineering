function dayIndex(text) {
    let mapper = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }
    let dayNames = Object.keys(mapper)
    
    if (!dayNames.includes(text)) {
        console.log('error');
        return
    }

    let index = mapper[text];
    console.log(index);
}

// dayIndex("Friday")