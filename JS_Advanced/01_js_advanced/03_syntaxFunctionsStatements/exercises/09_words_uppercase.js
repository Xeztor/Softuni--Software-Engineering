function upperCaseWords(text){
    const regex = /\w+/g;
    let words = text.match(regex);

    console.log(words.join(', ').toUpperCase())
}

// upperCaseWords('Hi, how are you?')
// upperCaseWords('hello')