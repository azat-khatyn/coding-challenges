def reversello(sentence):
    words = sentence.split()
    reversed_sen = []
    for w in range(len(words), 0, -1):
        reversed_sen.append(words[w - 1])
    return (' '.join(reversed_sen))


print(reversello('I like this program very much'))