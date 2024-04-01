def is_palindrome(input_string):
    input_string = input_string.lower()    
    return input_string == input_string[::-1]

input_str = "Amma"
if is_palindrome(input_str):
    print("palindrome")
else:
    print("Not palindrome")
