"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

import json


def is_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    for x in zip(sorted(word1), sorted(word2)):
        if x[0] != x[1]:
            return False
    return True


def group_anagrams(strs):
    if len(strs) <= 1:
        return [strs]

    result = []
    n = len(strs)
    i = 0
    while i < n:
        current_goup = [strs[i]]
        j = i+1
        while j < n:
            if is_anagrams(strs[i], strs[j]):
                current_goup.append(strs[j])
                strs.pop(j)
                n = len(strs)
            else:
                j += 1
        result.append(current_goup)
        i += 1
    return result


def group_anagrams_fast(strs):
    if len(strs) <= 1:
        return [strs]

    anagrams_lookup = {}
    for word in strs:
        word_sorted = "".join(sorted(word))
        if word_sorted not in anagrams_lookup:
            anagrams_lookup[word_sorted] = [word]
        else:
            anagrams_lookup[word_sorted].append(word)

    return [x for x in anagrams_lookup.values()]


example = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams_fast(example))


# with open("group_anagrams.data", "r") as fp:
#     long_example = json.load(fp)
# print(group_anagrams_fast(long_example))
