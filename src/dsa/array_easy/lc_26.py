"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
 such that each unique element appears only once. The relative order of the elements 
 should be kept the same.

Since it is impossible to change the length of the array in some languages,
 you must also return the new length of the array.

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

def remove_duplicates(nums :list) -> tuple:
    if len(nums) == 0:
        return (0, [])
    left_index = 0
    for right_index in range(1, len(nums)):
        if nums[left_index] != nums[right_index]:
            left_index += 1
            nums[left_index] = nums[right_index]
    return (left_index + 1, nums)

if __name__ == '__main__':
    nums = [0,0,1,2,3,4,4,4,5,6,6,7,10]
    print(remove_duplicates(nums=nums))