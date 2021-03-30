"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""


def top_k(nums, k):
    if len(nums) <= 1:
        return nums
    frequency_map = {}

    for n in nums:
        if n not in frequency_map:
            frequency_map[n] = 1
        else:
            frequency_map[n] += 1

    sorted_frequencies = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_frequencies[:k]]

nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]

print(top_k(nums, k))