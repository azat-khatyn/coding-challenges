"""
p = [2, 0, 1, 3]
a = [a, b, c, d]

result = [b, c, a, d]
"""


def apply_permutation(p, a):
    if len(p) != len(a):
        raise Exception("Error!")
    permuted_array = [0] * len(a)
    for i in range(len(a)):
        new_ind = p[i]
        print(new_ind)
        permuted_array[new_ind] = a[i]
    return permuted_array

p = [2, 0, 1, 3]
array = ['a', 'b', 'c', 'd']


print(apply_permutation(p, array))

def book_solution(perm, a):
    for i in range(len(a)):
        while perm[i] != i:
            a[perm[i]], a[i] = a[i], a[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

print(book_solution(p, array))