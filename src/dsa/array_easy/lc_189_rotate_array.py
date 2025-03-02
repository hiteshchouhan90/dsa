"""
https://leetcode.com/problems/rotate-array/description/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

def rotate_array(nums :list, k :int) -> list:
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    def reverse_list(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    reverse_list(0, n - 1)
    reverse_list(0, k - 1)
    reverse_list(k, n - 1 )
    return nums

if __name__ == '__main__':
    lst = [1,2,3,4]
    print(rotate_array(lst, 1))