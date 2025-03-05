"""
Count occurrences of a number in a sorted array with duplicates

https://www.geeksforgeeks.org/count-occurrences-of-a-number-in-a-sorted-array-with-duplicates/

Given a sorted array arr[] of size N and a number x. Find the number of occurrences of x in arr[].

Example 1:

Input:
N = 9
arr[] = {1, 2, 2, 2, 2, 3, 4, 4, 8}
x = 4
Output: 2
Explanation: 4 occurs 2 times in the given array.
"""

def num_occurences(nums :list, x :int) -> int:
    n = len(nums)
    left_index = 0
    right_index = n
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        if nums[mid_index] < x:
            left_index = mid_index + 1
        elif nums[mid_index] > x:
            right_index = mid_index
        else:
            left_count = mid_index
            right_count = mid_index
            while left_count >= 0 and nums[left_count] == x:
                left_count -= 1
            while right_count < n and nums[right_count] == x:
                right_count += 1
            return right_count - left_count - 1
    return 0


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 2, 3, 4, 4, 8]
    x = 4
    print(num_occurences(nums, x))