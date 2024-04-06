from flask import Flask, render_template, request, jsonify
from response import InterviewResponse
from loading_file import read_file
import pandas as pd


app = Flask(__name__)
finalTranscription = ''
response_array = []

df = pd.read_csv('questions.csv', encoding='latin-1')
# print(df.columns)

questions_selected = df.sample(n=5)

for _, row in questions_selected.iterrows():
    question = row['Questions']
    bad_example = row['BadExample']
    bad_blurb = row['BadBlurb']
    good_example = row['GoodExample']
    good_blurb = row['GoodBlurb']

    response_array.append(InterviewResponse(question,
                                            badexample=bad_example,
                                            badblurb=bad_blurb,
                                            goodexample=good_example,
                                            goodblurb=good_blurb))


def clear_array(current_array):
   current_array.clear()
   
@app.route('/send_text', methods=['POST'])
def receive_text():
    if request.is_json:
        data = request.get_json()  # Get data sent as JSON
        finalTranscription = data.get('text', '')  # Extract text field from JSON data or default to empty string
        if finalTranscription:
            print("Received text:", finalTranscription)  # Optional: log to console or process text as needed
            # setResponse(finalTranscription)
            return finalTranscription
            # return jsonify({"status": "success", "message": "Text received successfully"}), 200
        else:
            return jsonify({"status": "error", "message": "No text provided"}), 400
    else:
        return jsonify({"status": "error", "message": "Request must be JSON"}), 415

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/interview1")
def interview1():
    if len(response_array) > 0:
     question1 = response_array[0].question
    else:
        question1 = "No question available"
    return render_template("interview_1.html", question1=question1)

@app.route("/interview2")
def interview2():
    if len(response_array) > 0:
     question2 = response_array[1].question
    else:
        question2 = "No question available"
    return render_template("interview_2.html", question2=question2)

@app.route("/interview3")
def interview3():
    if len(response_array) > 0:
     question3 = response_array[2].question
    else:
        question3 = "No question available"
    return render_template("interview_3.html", question3=question3)

@app.route("/interview4")
def interview4():
    if len(response_array) > 0:
     question4 = response_array[3].question
    else:
        question4 = "No question available"
    return render_template("interview_4.html", question4=question4)

@app.route("/interview5")
def interview5():
    if len(response_array) > 0:
     question5 = response_array[4].question
    else:
        question5 = "No question available"
    return render_template("interview_5.html", question5=question5)

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)