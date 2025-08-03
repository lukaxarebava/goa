const myNumber = 7;

const button = document.getElementById("checkButton");

button.addEventListener("click", function() {
  const userGuess = parseInt(document.getElementById("userInput").value);

  if (userGuess === myNumber) {
    alert("შენ გამოიცანი ჩემი რიცხვი");
  } else {
    alert("შენ ვერ გამოიცანი ჩემი რიცხვი");
  }
});
