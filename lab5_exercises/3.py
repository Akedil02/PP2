import re

def find_underscore_sequences(input_string):
    pattern = r'_([a-z]+)_'
    matches = re.findall(pattern, input_string)
    
    if matches:
        print("match")
    else:
        print("no match")

