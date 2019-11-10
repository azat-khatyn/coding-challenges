lst1 = [1, 2, 3, 4, 5]

def find_two_numbers(k, lst):
    for i in range(0, (len(lst) - 1)):
        for j in range((i + 1), len(lst)):
            if lst[i] + lst[j] == k:
                return i, j
    return None

for k in range(-2, 15):
    print('%d: %s' % (k, str(find_two_numbers(k, lst1))))
