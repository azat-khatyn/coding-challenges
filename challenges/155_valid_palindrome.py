"""
case insensitive
Input: "A man, a plan, a canal: Panama"
Output: true
"""
import math

def is_palindrome(s):
    if len("s") == 0:
        return True
    s = s.lower()

    characters = s.strip().split()
    mid = math.ceil(len(characters)/2)
    for i in range(mid):
        if characters[i] != characters[-i-1]:
            return False
    return True


test = "A man, a plan, a canal: Panama"
print(is_palindrome(test))
