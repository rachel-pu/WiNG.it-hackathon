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
        self.badexample = badexample
        self.badblurb = badblurb
        self.goodexample = goodexample
        self.goodblurb = goodblurb

    def get_question(self):             # print question
       return self.question
    
    def set_responsetime(self, time):           # set indiv reponse time
        self.responsetime = time
        
    def get_time(self):                 # print indiv reponse time
        return self.responsetime
    
    def get_average_time(self, response_array):             # print average time
        average_time = sum(self.responsetime for response in response_array) / 5
        return average_time

    def get_top_words(self):           # print top words
        words = self.response.split()
        word_count = Counter(words)
        self.mostrepeatedwords = word_count.most_common(3)        # for each question
        return self.mostrepeatedwords

    def set_response(self, text):       # set response
        self.response = text

    def get_badexample(self):
        return self.badexample
    
    def get_badblurb(self):
        return self.badblurb

    def get_goodexample(self):
        return self.goodexample

    def get_goodblurb(self):
        return self.goodblurb
    
    

    



    


    
        

