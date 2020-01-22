def reverse_str(strg):
    return ''.join([strg[i] for i in range(len(strg) - 1, -1, -1)])


def reverse_str_recursive(strg):
    if len(strg) == 1:
        return strg
    return reverse_str_recursive(strg[1:]) + strg[0]

# abcd
# bcd
# cd
# d
# -> dc
# -> dcb
# -> dcba



strg1 = 'abcd'
strg1_rev = 'dcba'

result = reverse_str(strg1)
print(strg1_rev)
print(result)

if result == strg1_rev:
    print('done')
else:
    print('wrong')

print()

result_rec = reverse_str_recursive(strg1)
print(strg1_rev)
print(result_rec)

if result_rec == strg1_rev:
    print('rec done')
else:
    print('rec wrong')