
def from_txt(file):
    f = open(file, 'r')
    pre_text = []
    for line in f:
        pre_text.append(line.strip('\n'))
    return pre_text

def count_unique(text):
    unique_words = {}
    for string in text:
        words = string.split()
        for w in words:
            if w in unique_words:
                unique_words[w] += 1
            else:
                unique_words[w] = 1
    return unique_words

def count_top_k(dictionary, k):
    return sorted(dictionary, key=dictionary.get, reverse=True)[:k]


pre_text = from_txt('test_text.txt')
tab = count_unique(pre_text)
print(count_top_k(tab, 3))
