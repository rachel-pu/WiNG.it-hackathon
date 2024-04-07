let voices, utterance;
    function speakQuestion(question) {
  // Check if speech synthesis is supported by the browser
  if ('speechSynthesis' in window) {
    // Create a new instance of SpeechSynthesisUtterance
    utterance = new SpeechSynthesisUtterance(question);

    // Speak the question
    speechSynthesis.speak(utterance);
  } else {
    // If speech synthesis is not supported, alert the user
    alert('Sorry, speech synthesis is not supported by your browser.');
  }
}
