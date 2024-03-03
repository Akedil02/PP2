import re

def match_pattern(input_string):
    pattern = r'a.*b$'
    match_result = re.fullmatch(pattern, input_string)
    
    if match_result:
        print("match")
    else:
        print("no match")

match_pattern("acb")      # match
match_pattern("abc")      # match
match_pattern("a123b")    # match
match_pattern("ab")       # match
match_pattern("aB")       # no match
