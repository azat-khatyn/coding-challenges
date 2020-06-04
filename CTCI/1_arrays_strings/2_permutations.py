# # Given two strings, write a method to decide if one is the permutation of the other

def is_permutation_with_sort(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return False
    if len(string1) != len(string2):
        return False
    string1_sorted = sorted(string1)
    string2_sorted = sorted(string2)
    for i in range(len(string1_sorted)):
        if string1_sorted[i] != string2_sorted[i]:
            return False
    return True

def is_permutation_with_dict(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return False
    if len(string1) != len(string2):
        return False
    dict1 = {}
    dict2 = {}
    for char in string1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
    for char in string2:
        if char not in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1
    for c, freq1 in dict1.items():
        freq2 = dict2[c]
        if freq1 != freq2:
            return False
    return True


def test_is_permutation(string1, string2, expectedReturn):
    print('Strings: \'%s\' and \'%s\', expected: %s, got with sort: %s, got with dict: %s' % \
          (string1, string2, expectedReturn, is_permutation_with_sort(string1, string2), is_permutation_with_dict(string1, string2)))

test_is_permutation('abc', 'bca', True)
test_is_permutation('mama', 'amma', True)
test_is_permutation('a roza upala', 'na lapu azora ', False)
test_is_permutation('', '', False)
test_is_permutation('', 'abc', False)
test_is_permutation('abcdefg', 'abdegfc', True)

# 2 times sorted + 1 for loop ==> 2 nlogn + n --> O(nlogn)
# frequency map with dict - 3 times n --> O(n)

