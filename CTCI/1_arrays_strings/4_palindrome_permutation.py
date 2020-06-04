def palindrome_permutations(word):
    frequency_map = {}
    for w in word:
        if w not in frequency_map:
            frequency_map[w] = 1
        else:
            frequency_map[w] += 1
    one_odd_char = False
    for char, freq in frequency_map.items():
        if freq % 2 != 0:
            if not one_odd_char:
                one_odd_char = True
            else:
                return False
    return True


def test_palindrome_permutations(word, expectedReturn):
    print('Word \'%s\', expected  %s, got %s' % (word, expectedReturn, palindrome_permutations(word)))

test_palindrome_permutations('arozaupalanalapuazora', True)
test_palindrome_permutations('aoarzupaalnalapuzaoar', True)
test_palindrome_permutations('baab', True)
test_palindrome_permutations('abcdcba', True)
test_palindrome_permutations('abcdmffcba', False)
test_palindrome_permutations('abcdefg', False)

# O(n)