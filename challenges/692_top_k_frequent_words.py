"""

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

"""


def get_to_k_words(words, k):
    if len(words) <= 1:
        return words

    frequency_map = {}
    for word in words:
        if word not in frequency_map:
            frequency_map[word] = 1
        else:
            frequency_map[word] += 1

    sorted_frequencies_by_alphabet = sorted(frequency_map.items(), key=lambda x: x[0])
    sorted_frequencies_by_count = sorted(sorted_frequencies_by_alphabet, key=lambda x: x[1], reverse=True)
    print(sorted_frequencies_by_count)
    return [x[0] for x in sorted_frequencies_by_count[:k]]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
# Output: ["i", "love"]

print(get_to_k_words(words, k))