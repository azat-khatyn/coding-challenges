def majority(lst):
    n_by_2 = int(len(lst)/2)
    counter = {}
    print('N/2 for this list is %d' %n_by_2)
    for element in lst:
        if element in counter:
            counter[element] += 1
        else:
            counter[element] = 1

    sorted_elements = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(sorted_elements)
    m_element = sorted_elements[0][0]
    # if m_element > n_by_2:
    return m_element
    #else:
    #    return 0


lst1 = [2, 2, 1, 2, 3]
lst2 = [1, 4, 5, 1, 1, 1]
lst3 = [1]
lst4 = [1, 1]


print('For list 1 the result is %d' % majority(lst1))
print('For list 2 the result is %d' % majority(lst2))
print('For list 3 the result is %d' % majority(lst3))
print('For list 4 the result is %d' % majority(lst4))