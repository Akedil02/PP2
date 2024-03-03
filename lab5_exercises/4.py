import re

def find_uppercase_lowercase_sequences(input_string):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, input_string)
    
    if matches:
        print("match")
    else:
        print("no match")

input_text = "AcBc"
find_uppercase_lowercase_sequences(input_text)
