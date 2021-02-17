def buddy_string(a, b):
    """ Given two strings A and B of lowercase letters,
        return true if you can swap two letters in A so the result is equal to B,
        otherwise, return false.

        Swapping letters is defined as taking two indices i and j
        (0-indexed) such that i != j and swapping the characters at A[i] and A[j].
        For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

        Example 1:

    Input: A = "ab", B = "ba"
    Output: true
    Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

        """

    if a == b:
        a_sorted = sorted(a)
        for i in range(len(a_sorted)-1):
            if a_sorted[i] == a_sorted[i+1]:
                return True
        return False
    elif len(a) != len(b):
        return False
    else:
        swap_index_1 = None
        swap_index_2 = None
        for i in range(len(a)):
            if a[i] != b[i]:
                if swap_index_1 is None:
                    swap_index_1 = i
                elif swap_index_2 is None:
                    swap_index_2 = i
                else:
                    return False
        if swap_index_1 is None or swap_index_2 is None:
            return False
        return a[swap_index_1] == b[swap_index_2] and a[swap_index_2] == b[swap_index_1]


"""  A = "ab", B = "ba" --> True
     A = "aa", B = "aa" --> False
     A = "aaaaaaabc", B = "aaaaaaacb" --> True
    A = "", B = "aa" --> False
"""

print(buddy_string("ab", "ba"))
print(buddy_string("aa", "aa"))
print(buddy_string("aaaaaaabc", "aaaaaaacb"))
print(buddy_string("", "aa"))