def check(word):
    return word == word[::-1]


word1 = "madam"
word2 = "hello"

print(f'Is "{word1}" a palindrome? {is_palindrome(word1)}')
print(f'Is "{word2}" a palindrome? {is_palindrome(word2)}')