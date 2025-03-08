"""https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/
https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

"""

def search_rotated_array(nums :list, target :int) -> int:
    n = len(nums)
    if n == 0:
        return -1
    if n == 1:
        return 0 if nums[0] == target else -1
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


