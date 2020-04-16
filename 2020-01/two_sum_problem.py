def two_sum(k, lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == k:
                return (i, j)
    return (-1, -1)


example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
k = 2

print(two_sum(k, example))

