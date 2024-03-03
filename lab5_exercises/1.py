import re

def match_pattern(input_string):
    pattern = r'a*b*'
    match_result = re.fullmatch(pattern, input_string)
    
    if match_result:
        print("match")
    else:
        print("no match")

match_pattern("a")        # match
match_pattern("ab")       # match
match_pattern("abb")      # match
match_pattern("ac")       # no match
match_pattern("bcd")      # no match
match_pattern("abcde")    # no match
