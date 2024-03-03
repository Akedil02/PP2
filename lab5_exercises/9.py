import re

def insert_space_before_uppercase(input_string):
    result_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return result_string

input_text = "ThisIsCamelCaseString"
output_text = insert_space_before_uppercase(input_text)


