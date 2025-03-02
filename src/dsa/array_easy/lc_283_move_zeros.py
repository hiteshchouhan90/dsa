"""
https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
def move_zeros(nums :list) -> list:
    if len(nums) == 0:
        return nums
    left_index = 0
    for right_index in range(len(nums)):
        if nums[right_index] != 0:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
    return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(move_zeros(nums=nums))