"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def two_sum(array, target):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]


def two_sum_2(array, target):
    values = {array[i]: i for i in range(len(array))}
    for i in range(len(array)):
        key = target - array[i]
        if key in values and i != values[key]:
            return [i, values[key]]


example = [2,7,11,15]
target = 18

print(two_sum(example, target))
print(two_sum_2(example, target))