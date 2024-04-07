
    // variables
    const button = document.getElementById('microphone-button'); // const button is getting html button element
    // const transcription = document.getElementById('transcription');
    let finalTranscript = '';
    let speechTime = 0;
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
        // transcription.textContent = finalTranscript; // Update the page with the transcription
    };

    speech.onend = function() {
        if (finalTranscript !== '') {
            // Prepare form data
            let formData = new FormData();
            formData.append('text', finalTranscript);
            formData.append('time', speechTime.toString()); // Convert time to string if necessary

            // Send the complete transcription and the speech time when the speech recognition stops
            fetch('/send_text', {
                method: 'POST',
                body: formData  // Sending as FormData object
            })
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
        }
    };

    button.onclick = () => {
        if (speechActive) {
            clearInterval(timerInterval);       // clear the timer when stop recording
            speech.stop();
            speechTime = totalSeconds;
            button.innerHTML = '<img class = "microphone-image" src="/static/images/microphone.png" alt="microphone image">';
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

