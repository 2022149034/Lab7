import pandas as pd

def count_alphabet_occurrences_pandas(text):
    filtered_text = ''.join(filter(str.isalpha, text)).lower()

    series = pd.Series(list(filtered_text))

    letter_counts = series.value_counts()

    return letter_counts

input_file_path_2 = 'input_7_2.txt' 
with open(input_file_path_2, 'r') as file:
    input_content_2 = file.read()

alphabet_occurrences_pandas = count_alphabet_occurrences_pandas(input_content_2)
print(alphabet_occurrences_pandas)
