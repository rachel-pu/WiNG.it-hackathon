
    // variables
    const button = document.getElementById('microphone-button'); // const button is getting html button element
    const transcription = document.getElementById('transcription');
    let finalTranscript = '';
    let speechActive = false; // tracking if microphone is recording, defaulted to false
    let speech = new webkitSpeechRecognition() || new SpeechRecognition();
    speech.continuous = true; // will continue to listen to user
    speech.interimResults = false;
    speech.lang = 'en-US';

    let timerInterval; // store interval timer
    let totalSeconds = 0; // store total seconds

    speech.onresult = function(event) {
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript + ' ';
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }
        transcription.textContent = finalTranscript; // Update the page with the transcription
    };

    speech.onend = function() {
        if (finalTranscript !== '') {
            // Send the complete transcription when the speech recognition stops
            fetch('/send_text', {
                method: 'POST',
//                headers: {
//                    'Content-Type': 'application/json',
//                },
                body: JSON.stringify({text: finalTranscript})
            })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
        }
    };

    button.onclick = () => {
        if (speechActive) {
            clearInterval(timerInterval);       // clear the timer when stop recording
            speech.stop();
            button.textContent = 'Start Recording';
        } 
        
        else {
            startTimer();       // start the timer when start recording
            speech.start();
            button.textContent = 'Stop Recording';
        }
        speechActive = !speechActive;
    };

    function startTimer() {     // start timer
        totalSeconds = 0;
        timerInterval = setInterval(() => {
            totalSeconds++;
            console.log(totalSeconds);
        }, 1000);      // 1000ms = 1s
    }

