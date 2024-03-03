import re

def split_by_uppercase(input_string):
    words = re.findall('[A-Z][^A-Z]*', input_string)
    result_string = ' '.join(words)
    return result_string

input_text = "ThisIsCamelCaseString"
output_text = split_by_uppercase(input_text)
