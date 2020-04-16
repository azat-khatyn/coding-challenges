"""
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment
which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.

"""


class Solution(object):
    # create function that test the size of the integer
    def reverse(self, x):
        def test_size(x):
            if x < -2**31 or x >= 2**31:
                return 0
            else:
                return x

    # test the size of the integer
        if test_size(x) == 0:
            return 0

    # handle negative integers
        if x < 0:
            minus = '-'
            strg = str(x)[1:]
        else:
            minus = ''
            strg = str(x)

    # reverse string order
        n = len(strg)
        rev = ''.join([strg[n - (i + 1)] for i in range(n)])
        
    # check for zeros at the beginning
        for i in range(n):
            if rev[i] != '0':
                rev = rev[i:]
                break
        return test_size(int(minus+rev))