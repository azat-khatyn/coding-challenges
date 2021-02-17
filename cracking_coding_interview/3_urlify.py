def urlify(str, str_len):
    j = len(str) - 1
    for i in range(str_len-1, -1, -1):
        if str[i] != ' ':
            str[j] = str[i]
            j -= 1
        else:
            str[j] = '0'
            j -= 1
            str[j] = '2'
            j -= 1
            str[j] = '%'
            j -= 1
    return str

str = 'Mr John Smith    '

print("".join(urlify(list(str), 13)))
