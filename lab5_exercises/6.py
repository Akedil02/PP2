import re

def replace_characters(input_string):
    result_string = re.sub(r'[ ,.]', ':', input_string)
    return result_string

input_text = "Hello, world. "
output_text = replace_characters(input_text)


