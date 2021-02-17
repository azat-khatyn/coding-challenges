"""
input = [2, 3, 5, 5, 5, 7, 11, 11, 11, 13]
output = 6
"""

# My Solution
def remove_dup(sorted_array):
    i = 0
    while i < len(sorted_array)-1:
        if sorted_array[i] == sorted_array[i+1]:
            sorted_array.remove(sorted_array[i+1])
        else:
            i += 1
    return len(sorted_array)

# Book solution
def elegant_solution(sorted_array):
    write_index = 1
    for i in range(1, len(sorted_array)):
        if sorted_array[write_index-1] != sorted_array[i]:
            sorted_array[write_index] = sorted_array[i]
            write_index += 1
    return write_index


input_test1 = [2, 3, 5, 5, 7, 11, 11, 11, 13, 13]
input_test2 = [2, 3, 5, 5, 7, 11, 11, 11, 13, 13]

print(remove_dup(input_test1))
print(elegant_solution(input_test2))