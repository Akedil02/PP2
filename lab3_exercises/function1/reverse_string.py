def reverse_words(input_string):
    words = input_string.split()

    reversed_words = reversed(words)

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

user_input = input("Enter a sentence: ")

result = reverse_words(user_input)
print("Reversed sentence:", result)
