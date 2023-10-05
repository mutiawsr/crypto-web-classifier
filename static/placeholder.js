var input = document.getElementById("input_text");
var phrases = ["Cryptocurrency yearly report 2021", "Bitcoin down by 10%", "Ethereum rise by 20%, analysts reported"];
var currentPhrase = 0;
var typingInterval;

function typingAnimation() {
  var text = phrases[currentPhrase];
  var i = 0;

  typingInterval = setInterval(function() {
    input.placeholder = text.substring(0, i);

    i++;

    if (i > text.length) {
      clearInterval(typingInterval);
      currentPhrase++;
      if (currentPhrase >= phrases.length) {
        currentPhrase = 0;
      }
      setTimeout(typingAnimation, 1500); // Delay before starting the next animation
    }
  }, 50);
}

typingAnimation();
