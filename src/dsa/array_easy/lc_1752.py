"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.
"""

def check_sorted_array(nums :list) -> bool:
    dip = 0
    for i in range(len(nums)):
        if nums[(i+1)%len(nums)] < nums[i]:
            dip += 1
        if dip > 1:
            return False
    return True


if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(check_sorted_array(nums))

    nums = [2,1,3,4]
    print(check_sorted_array(nums))

    nums = [1,2,3,4]
    print(check_sorted_array(nums)) 

    nums = [1,1,1,1]
    print(check_sorted_array(nums))


