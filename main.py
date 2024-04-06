from response import InterviewResponse
from loading_file import read_csv
import pandas as pd

def main():
    df = pd.read_csv('questions.csv', encoding='latin-1')
    print(df)

    questions_selected = df.sample(n=5)

    response_array = []

    for _, row in questions_selected.iterrows():
        response_array.append(InterviewResponse(row['Questions'], **row.to_dict))    

    for response in response_array: 
        print(response.question)


def print_information(response_array, row_index, col):
    response = response_array[row_index]
    text = response.print_csv_info(col)

if __name__ == "__main__":
    main()

