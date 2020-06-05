def string_compression(strg):
    compressed_string = []
    count = 0
    curr_char = strg[0]
    for i in range(len(strg)):
        if strg[i] == curr_char:
            count += 1
        else:
            compressed_string.append(curr_char + str(count))
            count = 1
            curr_char = strg[i]
    compressed_string.append(curr_char + str(count))
    result = ''.join(compressed_string)
    if len(result) < len(strg):
        return result
    else:
        return strg


def test_string_comprassion(strg, expextedOutput):
    print('For \'%s\' compressed string is \'%s\', expected \'%s\'' % (strg, string_compression(strg), expextedOutput))


test_string_comprassion('sstttriinngggg', 's2t3r1i2n2g4')
test_string_comprassion('aabb', 'aabb')
test_string_comprassion('aaaa', 'a4')
test_string_comprassion('a', 'a')

# test_string_comprassion()
# test_string_comprassion()