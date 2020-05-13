def binary_search(lst, x):
    if len(lst) == 0:
        return -1

    start = 0
    end = len(lst) - 1

    while start <= end:
        # avoiding integer overflow by replacing (end + start)/2 by -->
        mid = int(end - (end - start)/2)
        print('Checking %d on index %d' % (lst[mid], mid))
        if lst[mid] == x:
            return mid
        if lst[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


lst1 = [0, 3, 5, 8 , 9 , 10 , 14, 15, 19 , 20]
print(lst1)
print('Lst1, x = 2, result = %d' % binary_search(lst1, 2))
print('Lst1, x = 19, result = %d' % binary_search(lst1, 19))
print('Lst1, x = 5, result = %d' % binary_search(lst1, 5))
print('Lst1, x = 25, result = %d' % binary_search(lst1, 25))
print('Lst1, x = -5, result = %d' % binary_search(lst1, -5))
print('Lst1, x = 9, result = %d' % binary_search(lst1, 9))
print()

lst2 = []
print(lst2)
print('Lst2, x = 7, result = %d' % binary_search(lst2, 7))
print()

lst3 = [4]
print(lst3)
print('Lst3, x = 4, result = %d' % binary_search(lst3, 4))
print('Lst3, x = 2, result = %d' % binary_search(lst3, 2))
print()
