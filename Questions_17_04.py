# Given a list of words, return a new list containing only the words that are palindromes, converted to uppercase.
#
# A palindrome reads the same forward and backward.

words = ["level", "python", "madam", "code", "radar"]
def isPalindrome(word):
    if len(word) == 0:
        return True
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] == word[j]:
            i+=1
            j-=1
        else:
            return False
    return True

# Iterative method
result = []
for item in words:
    if isPalindrome(item):
        result.append(item.upper())
print(result)
    
# Using List Comprehension
print([x.upper() for x in words if isPalindrome(x)])



# Write a function that takes a string and returns all duplicate characters along with their counts.
# Requirements
# Case-insensitive ("A" and "a" are the same)
# Ignore spaces
# Return a dictionary where:
# key = duplicated character
# value = number of occurrences
# Only include characters that appear more than once
# input_string = "Programming"
# Example:
# {
#     "r": 2,
#     "g": 2,
#     "m": 2
# }

input_string = "Programming" 
result = dict()
for ch in input_string:
    result[ch] = result.get(ch,0) + 1
    
print({k:v for k,v in result.items() if v > 1})