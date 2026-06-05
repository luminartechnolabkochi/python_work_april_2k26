
def is_palindrome(word):

    reversed_word = word[::-1]

    return word == reversed_word

print(is_palindrome("madam")) 
print(is_palindrome("dam")) # dam == mad 

