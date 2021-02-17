def hanoi(n, source, target, spare):
    if n > 0:
        hanoi(n-1, source, spare, target)
        target.append(source.pop())
        hanoi(n-1, spare, target, source)


A = [1, 2, 3, 4, 5]
B = []
C = []

hanoi(5, A, C, B)

print(A)
print(B)
print(C)

