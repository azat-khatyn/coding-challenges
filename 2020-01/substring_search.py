def substring(txt, substring):
    for i in range(len(txt)):
        found = True
        for j in range(len(substring)):
            if (i+j) == len(txt) or txt[i +j] != substring[j]:
                found = False
                break
        if found == True:
            return i
    return -1

text = 'abcd'
sbstr = 'cde'


print(substring(text, sbstr))
