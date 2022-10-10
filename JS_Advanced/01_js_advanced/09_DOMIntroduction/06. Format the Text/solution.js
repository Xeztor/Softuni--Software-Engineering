function solve() {
  let inputText = document.getElementById("input").value;
  let sentences = inputText.split('.').map(sentence => sentence.trim());
  let filteredSentences = sentences.filter(sentence => sentence !== '');
  let finalSentences = filteredSentences.map(sentence => sentence + '.')
  let choppedSentences = finalSentences.reduce((resultArray, item, index) => {
    const chunkIndex = Math.floor(index / 3)

    if (!resultArray[chunkIndex]) {
      resultArray[chunkIndex] = [] // start a new chunk
    }

    resultArray[chunkIndex].push(item)

    return resultArray
  }, [])

  let outputDiv = document.getElementById("output");
  for (let paragraphSentences of choppedSentences) {
    outputDiv.innerHTML += `<p>${paragraphSentences.join('')}</p>`
  };
}