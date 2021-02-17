import math


def abs_sort(arr):
    d = {}
    for element in arr:
        if element < 0:
            if -element in d:
                d[-element] += 1
            else:
                d[-element] = 1

    for i in range(len(arr)):
        arr[i] = int(math.fabs(arr[i]))
    arr.sort()

    for i in range(len(arr)):
        if arr[i] in d and d[arr[i]] > 0:
            arr[i] = -arr[i]
            d[-arr[i]] -= 1

    return arr  # your code goes here
'''
input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
'''

l = [2, -7, -2, -2, 0]
print(abs_sort(l))