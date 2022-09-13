function stringLenghtAnalyze(text1, text2, text3) {
    let lengthSum = 0;
    let allTexts = [text1, text2, text3]
    for (i = 0; i < 3; i++) {
        lengthSum += allTexts[i].length;
    }
    console.log(lengthSum);

    let avarege = Math.floor(lengthSum / 3);

    console.log(avarege)
}
