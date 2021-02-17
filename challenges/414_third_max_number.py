"""
Given integer array nums, return the third maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

"""

def thirdMax(self, nums: List[int]):
    unique_values = set(nums)
    unique_list = sorted(list(unique_values))
    if len(unique_list) >= 3:
        return unique_list[-3]
    else:
        return unique_list[-1]
