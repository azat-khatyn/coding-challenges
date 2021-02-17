def compare_with_different_len(long, short):
    if len(long) - len(short) > 1:
        return False
    one_diff = False
    j = 0
    for i in range(len(long)):
        if long[i] != short[j]:
            if not one_diff:
                one_diff = True
            else:
                return False
        else:
            j += 1
            if j == len(short) and not one_diff:
                break
    return True


def compare_with_same_len(str1, str2):
    one_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if not one_diff:
                one_diff = True
            else:
                return False
    return True


def one_away(str1, str2):
    if len(str1) > len(str2):
        return compare_with_different_len(str1, str2)
    elif len(str2) > len(str1):
        return compare_with_different_len(str2, str1)
    else:
        return compare_with_same_len(str1, str2)


def test_one_away(str1, str2, expectedValue):
    print('For \'%s\' and \'%s\' expected %s, got %s' % (str1, str2, expectedValue, one_away(str1, str2)))


test_one_away('pale', 'ple', True)
test_one_away('ple', 'pale', True)
test_one_away('pales', 'pale', True)
test_one_away('pale', 'pales', True)
test_one_away('pale', 'bale', True)
test_one_away('bale', 'pale', True)
test_one_away('pale', 'bake', False)
test_one_away('bake', 'pale', False)
test_one_away('apale', 'pale', True)
test_one_away('pale', 'apale', True)
test_one_away('pallle', 'pale', False)
test_one_away('pale', 'pallle', False)
test_one_away('pale', 'paleee', False)
test_one_away('ppale', 'paleg', False)
test_one_away('', '', True)
test_one_away('a', 'a', True)
test_one_away('a', 'b', True)
test_one_away('b', 'a', True)
test_one_away('ab', 'a', True)
test_one_away('ab', '', False)


# O(n)