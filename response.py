from collections import Counter
import pandas as pd

class InterviewResponse:
    
    # each object will be a question and traits
    
    def __init__(self, question, badexample=None, badblurb=None, goodexample=None, goodblurb=None):
        self.question = question                    # question 
        self.response = ""                          # answer recorded from the audio
        self.responsetime = None                   # will be recorded with timer?
        self.mostrepeatedwords = None             # for each question?
        self.tone = None
        self.badexample = None
        self.badblurb = None
        self.goodexample = None
        self.goodblurb = None

    def word_count(self):

        words = self.response.split()
        word_count = Counter(words)
        self.mostrepeatedwords = word_count.most_common(5)        # for each question


    def print_question(self):           # for printing question on website
        question = self.question

    def print_average_time(self, response_array):
        average_time = sum(self.responsetime for response in response_array) / 5

    def print_most_repeated(self):
        words = self.response.split()
        word_count = Counter(words)
        self.mostrepeatedwords = word_count.most_common(5) 

    def print_badexample(self):
        badexample = self.badexample
    
    def print_badexample(self):
        badblurb = self.badblurb

    def print_goodexample(self):
        goodexample = self.goodexample

    def print_goodblurb(self):
        goodblurb = self.goodblurb


    
        

