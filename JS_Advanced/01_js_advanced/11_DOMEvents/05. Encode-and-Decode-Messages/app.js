function encodeAndDecodeMessages() {
    let [encodeDiv, decodeDiv] = document.querySelectorAll('#container div');
    encodeDiv.getElementsByTagName("button")[0].addEventListener('click', encode);
    decodeDiv.getElementsByTagName("button")[0].addEventListener('click', decode);


    function encode() {
        let encodeTextArea = encodeDiv.getElementsByTagName("textarea")[0];
        let textToEncode = encodeTextArea.value;
        let encodedArray = Array.from(textToEncode).map(char => char.charCodeAt(0) + 1);
        let encodedString = String.fromCharCode(...encodedArray)

        decodeDiv.getElementsByTagName('textarea')[0].textContent = encodedString;
        encodeTextArea.value = '';
    };

    function decode() {
        let decodeTextArea = decodeDiv.getElementsByTagName("textarea")[0];
        let textToDecode = decodeTextArea.value;
        let decodedArray = Array.from(textToDecode).map(char => char.charCodeAt(0) - 1);
        let decodedString = String.fromCharCode(...decodedArray)

        decodeTextArea.value = decodedString;
    };
}