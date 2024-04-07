import pandas as pd

class InterviewResponse:
    
    # each object will be a question and traits
    
    def __init__(self, question, badexample=None, badblurb=None, goodexample=None, goodblurb=None):
        self.question = question                    # question 
        self.tone = None
        self.badexample = badexample
        self.badblurb = badblurb
        self.goodexample = goodexample
        self.goodblurb = goodblurb

    def get_question(self):             # print question
        return self.question
    

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
    
    

    



    


    
        

