from collections import Counter
import pandas as pd

class InterviewResponse:
    
    # each object will be a question and traits
    
    def __init__(self, question):
        self.question = question                    # question 
        self.response = ""                          # answer recorded from the audio
        self.response_time = None                   # will be recorded with timer?
        self.most_repeated_words = None             # for each question?
        self.tone = None
        self.csv_info = kwargs


    def word_count(self):

        words = self.response.split()
        word_count = Counter(words)
        self.most_repeated_words = word_count.most_common(5)        # for each question


    def print_question(self):           # for printing question on website
        question = self.question

    def print_average_time(self, response_array):
        average_time = sum(self.response_time for response in response_array) / 5

    def print_most_repeated(self):
        words = self.response.split()
        word_count = Counter(words)
        self.most_repeated_words = word_count.most_common(5) 

    def print_csv_info(self, col):
        information = self.csv_info[col]

