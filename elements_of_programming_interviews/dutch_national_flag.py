"""
A = [0, 1, 3, 0, 2, 1, 1]
i = 2

output: [0, 0, 1, 2, 2, 1, 1]

"""

def quicksort(A, index):
    less_then_pivot = []
    equal_to_pivot = []
    greater_then_pivot = []
    pivot = A[index]

    for element in A:
        if element == pivot:
            equal_to_pivot.append(element)
        elif element < pivot:
            less_then_pivot.append(element)
        else:
            greater_then_pivot.append(element)
    return less_then_pivot+equal_to_pivot+greater_then_pivot


A = [0, 1, 3, 0, 2, 1, 1]
i = 2
print(quicksort(A, i))




