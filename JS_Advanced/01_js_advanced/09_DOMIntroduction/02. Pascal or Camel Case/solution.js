function solve() {
  let result = document.getElementById("result");

  let namingConvention = document.getElementById("naming-convention").value;

  if (namingConvention !== "Camel Case" &&
    namingConvention !== "Pascal Case") {
    result.textContent = "Error!";
    return;
  };
  let text = document.getElementById("text").value;
  let words = text.split(" ");
  let uppercaseWords = words.map(element => element[0].toUpperCase() + element.substring(1).toLowerCase());


  if (namingConvention == "Camel Case") {
    uppercaseWords[0] = uppercaseWords[0].toLowerCase();
  };

  result.textContent = uppercaseWords.join("");
}