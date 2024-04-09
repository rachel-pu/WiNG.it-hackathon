from flask import Flask, render_template, request, jsonify
from response import InterviewResponse
from loading_file import read_file
import pandas as pd
from collections import Counter


app = Flask(__name__)
finalTranscription = ''
finalTime = 0

question_array = []
transcripts_array = []
minutes_array = []
seconds_array = []

df = pd.read_csv('questions.csv', encoding='latin-1')

def clear_array():
    if len(question_array) > 0:
        question_array.clear()
        transcripts_array.clear()
        minutes_array.clear()
        seconds_array.clear()


def set_array():
    questions_selected = df.sample(n=5)
    for _, row in questions_selected.iterrows():
        question = row['Questions']
        bad_example = row['BadExample']
        bad_blurb = row['BadBlurb']
        good_example = row['GoodExample']
        good_blurb = row['GoodBlurb']

        question_array.append(InterviewResponse(question,
                                                badexample=bad_example,
                                                badblurb=bad_blurb,
                                                goodexample=good_example,
                                                goodblurb=good_blurb))


@app.route('/send_text', methods=['POST'])
def receive_text():
    finalTranscription = request.form['text']  # Retrieve text from form data
    finalTime = request.form['time']  # Retrieve time from form data
    print("Received transcription:", finalTranscription)
    print("Speech duration:", finalTime, "seconds")
    transcripts_array.append(finalTranscription)
    temp_array = []
    temp_array.append(finalTime)
    for time in temp_array:
        minutes = int(time) // 60
        seconds = int(time) % 60
        minutes_array.append(minutes)
        seconds_array.append(seconds)

    return jsonify({"status": "success", "message": "Data received"})


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/instructions")
def instructions():
    clear_array()
    set_array()
    return render_template("instructions.html")



@app.route("/interview1")
def interview1():
    if len(question_array) > 0:
        question1 = question_array[0].question
    else:
        question1 = "No question available"
    return render_template("interview_1.html", question1=question1)


@app.route("/interview2")
def interview2():
    if len(question_array) > 0:
        question2 = question_array[1].question
    else:
        question2 = "No question available"
    return render_template("interview_2.html", question2=question2)


@app.route("/interview3")
def interview3():
    if len(question_array) > 0:
        question3 = question_array[2].question
    else:
        question3 = "No question available"
    return render_template("interview_3.html", question3=question3)


@app.route("/interview4")
def interview4():
    if len(question_array) > 0:
        question4 = question_array[3].question
    else:
        question4 = "No question available"
    return render_template("interview_4.html", question4=question4)


@app.route("/interview5")
def interview5():
    if len(question_array) > 0:
        question5 = question_array[4].question
    else:
        question5 = "No question available"
    return render_template("interview_5.html", question5=question5)


@app.route("/results")
def results():
    return render_template("results.html", question_array=question_array, transcripts_array=transcripts_array, minutes_array=minutes_array, seconds_array=seconds_array)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

#     app.run(debug=True)