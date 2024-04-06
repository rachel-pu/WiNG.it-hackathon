import csv
import random
import time
import speech_recognition as sr
from collections import Counter
import pandas as pd

class InterviewResponse:
    
    # each object will be a question and traits
    
    def __init__(self, question):
        self.question = question                    # question 
        self.response = ""                          # answer recorded from the audio
        self.response_time = None                   # will be recorded with timer?
        self.filler_count = None                    # to be aggregated later
        self.most_repeated_words = None             # for each question?
        self.tone = None

    def word_count(self):

        words = response.split()
        word_count = Counter(words)
        self.most_repeated_words = word_count.most_common(5)        # for each question

        fillers = ["um", "uh", "like", "so"]
        self.filler_count = sum(word_count.get(filler, 0) for filler in fillers)
    

def save_to_array():
        

# read questions from a CSV file
def read_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            questions.append(row[0])  
    return questions

def listen_and_record_response():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something")
        audio = r.listen(source)
        try:
            response = r.recognize_google(audio)
            return response.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""


csv_file_path = "questions.csv"
all_questions = read_questions_from_csv(csv_file_path)
random.shuffle(all_questions)
selected_questions = all_questions[:5]

interview = InterviewResponse(selected_questions)

for i, question in enumerate(interview.questions):
    print(f'Question {i+1}: {question}')
    response = listen_and_record_response()
    response_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    interview.record_response(i, response, response_time)

interview.analyze_responses()

responses_data = interview.get_responses_data()
for response_data in responses_data:
    print(response_data)
