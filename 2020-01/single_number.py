def single_number(lst):
    set1 = set()
    set2 = set()

    for element in lst:
        if element not in set1:
            set1.add(element)
        else:
            set2.add(element)

    for element in set1:
        if element not in set2:
            return element
    return None


lst1 = [1, 2, 2, 3, 3, 4, 4]
lst2 = [1]
lst3 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
lst4 = [3, 4, 5, 5, 4, 3, 1]


print('For list1 the single number is %d' % single_number(lst1))
print('For list2 the single number is %d' % single_number(lst2))
print('For list3 the single number is %d' % single_number(lst3))
print('For list4 the single number is %d' % single_number(lst4))