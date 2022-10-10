function toggle() {
    let toggleBtn = document.querySelector("span.button");

    let extraTextElement = document.getElementById("extra");

    if (toggleBtn.textContent == "More") {
        extraTextElement.style.display = 'block';
        toggleBtn.textContent = "Less";
    } else {
        extraTextElement.style.display = 'none';
        toggleBtn.textContent = "More";
    };
}