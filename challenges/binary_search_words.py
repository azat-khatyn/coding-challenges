def look_up(word, words):
    left = 0
    right = len(words)-1
    while left <= right:
        mid = int((left+right)/2)
        if words[mid] == word:
            return mid
        if word < words[mid]:
            right = mid-1
        else:
            left = mid + 1
    return -1


lookup = ["interviews", "are", "not", "nice", "to", "prepare", "for", "zena", "ant"]
words = ["slava", "yana", "not", "masha", "interviews", "word", "are", "nice", "to"]
words.sort()
print(words)

for word in lookup:
    print(word, look_up(word, words))



