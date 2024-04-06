from response import InterviewResponse
from loading_file import read_file
import pandas as pd

response_array = []
def main():
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

    # for i in response_array:
    #     print("Question:", i.question)
    #     print("Bad Example:", i.badexample)
    #     print("Bad Blurb:", i.badblurb)
    #     print("Good Example:", i.goodexample)
    #     print("Good Blurb:", i.goodblurb)
    #     print()

def get_response_array():
    return response_array
    
# if __name__ == "__main__":
#     main()

