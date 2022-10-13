function solve() {
  const rigthAnswers = [
    "onclick",
    "JSON.stringify()",
    "A programming API for HTML and XML documents"
  ]

  const sectionGen = sectionGenerator();

  Array.from(document.getElementsByClassName("answer-wrap"))
    .forEach(p => p.addEventListener('click', saveAnswer));

  let answers = [];

  function saveAnswer(event) {
    let answer = event.target.textContent;
    answers.push(answer);

    let currentSection = event.target.closest('section');

    changeQuestion(currentSection);
  };

  function changeQuestion(currentSection) {
    currentSection.style.display = 'none';

    let nextSectionObj = sectionGen.next();

    if (nextSectionObj.done) {
      showResult()
      return;
    };

    let sectionElement = nextSectionObj.value;
    sectionElement.style.display = 'block';

  };

  function showResult() {
    let resultUl = document.getElementById("results");
    resultUl.style.display = 'block';
    let resulth1 = resultUl.getElementsByTagName("h1")[0];

    let quizzResult = getResult(answers);

    if (quizzResult === rigthAnswers.length) {
      resulth1.textContent = "You are recognized as top JavaScript fan!";
    } else {
      resulth1.textContent = `You have ${quizzResult} right answers.`
    };

  };

  function getResult(answers) {
    let result = 0;
    for (let answer of answers) {
      if (rigthAnswers.includes(answer)) {
        result += 1;
      };
    };

    return result;
  };

  function* sectionGenerator() {
    let sections = Array.from(document.getElementsByTagName('section')).slice(1);
    for (let section of sections) {
      yield section;
    };
  };
}
