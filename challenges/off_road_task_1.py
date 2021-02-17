'''
Input: 'aaaabbbcca'
Output: [('a', 4), ('b', 3), ('c', 2), ('a', 1)]
'''


def off_road(a):
    counter = 1
    result = []
    n = len(a)
    for i in range(n-1):
        if a[i] == a[i+1]:
            counter += 1
        else:
            result.append((a[i], counter))
            counter = 1
    result.append((a[n-1], counter))
    return result


test = 'aaaabbbccd'
print(off_road(test))
