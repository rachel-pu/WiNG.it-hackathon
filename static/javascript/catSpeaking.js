var voices, utterance;
function speakQuestion(question) {
  // stop any speaking in progress
  window.speechSynthesis.cancel();

  // Wait for the voices to be loaded
  window.speechSynthesis.onvoiceschanged = function() {
    // Get the voices
    voices = window.speechSynthesis.getVoices();

    // Find the Google UK English Male voice
    var googleUKMaleVoice = voices.find(function(voice) {
      return voice.name === 'Google UK English Male';
    });

      // create new utterance with all the properties
      utterance = new SpeechSynthesisUtterance(question);

      // Set the voice
      utterance.voice = googleUKMaleVoice;

      // speak that utterance
      window.speechSynthesis.speak(utterance);

  };
}
