"""
Input: x = 123
Output: 321

"""


def reverse_int(x):
    minus = x < 0
    x = abs(x)
    int_to_str = list(str(x))
    for i in range(0, int(len(int_to_str)/2)):
        int_to_str[i], int_to_str[-i-1] = int_to_str[-i-1], int_to_str[i]
    result = int("".join(int_to_str))
    if minus:
        result = -result
    return 0 if result > (2**31 - 1) or result < -(2 ** 31) else result


# Older version

  # temp = int_to_str[i]
        # int_to_str[i] = int_to_str[-i-1]
        # int_to_str[-i - 1] = temp

x = 123456789
y = 123456

print(reverse_int(x))
print(reverse_int(y))
print(reverse_int(1))