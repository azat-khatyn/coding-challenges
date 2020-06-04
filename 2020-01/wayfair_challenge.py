def solution(A):

    # check trivial case
    if len(A) == 1:
        return -1

    # collect a map of values to indices
    value_to_indices = {}
    for i in range(len(A)):
        a = A[i]
        if a not in value_to_indices:
            value_to_indices[a] = []
        value_to_indices[a].append(i)

    # sort by values
    value_to_indices_sorted = sorted(value_to_indices.items(), key=lambda x: x[0])

    # all values were the same
    if len(value_to_indices_sorted) == 1:
        return -1

    # consider each adjacent pair and find the combination of indices with the smallest distance
    min_distance = 40000
    for i in range(len(value_to_indices_sorted) - 1):
        t1 = value_to_indices_sorted[i]
        t2 = value_to_indices_sorted[i + 1]
        for k1 in t1[1]:
            for k2 in t2[1]:
                distance = abs(k1 - k2)
                if distance < min_distance:
                    min_distance = distance
    return min_distance


lst = [1, 4, 7, 3, 3, 5]
print(solution(lst))

lst = [1]
print(solution(lst))

lst = [1, 1, 1, 1, 1]
print(solution(lst))

lst = [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 7, 2]
print(solution(lst))

lst = [2147483647, -2147483648, 0]
print(solution(lst))

lst = [11, 1, 4, 7, 20, 3, 3, 5, 9, 15, 4, 9, 12, 4]
print(solution(lst))

lst = [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2]
print(solution(lst))
