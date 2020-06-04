#Implement an algorithm to determine if a string has all unique characters

def unique(strg):
    if len(strg) == 1:
        return True
    if len(strg) == 0:
        return False
    unique_chars = set()
    for char in strg:
        if char not in unique_chars:
            unique_chars.add(char)
        else:
            return False
    return True


def test_unique(strg, expectedIsUnique):
    isUnique = unique(strg)
    print('String: %s, expected: %s, got: %s' % (strg, expectedIsUnique, isUnique))


test_unique('aaaaa', False)
test_unique('abcddef', False)
test_unique('abcdefg', True)
test_unique("", False)
test_unique('a', True)

# Alternatives:
# brute force - two for loops, O(n^2)
# using sort - complexity of sort O(nlogn + n) ==> O(nlogn)

