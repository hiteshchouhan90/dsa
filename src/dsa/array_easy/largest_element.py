"""Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr[] = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.
Input: arr[] = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.
Input: arr[] = [10]
Output: 10
Explanation: There is only one element which is the largest.
Constraints:
1 <= arr.size()<= 106
0 <= arr[i] <= 106

https://www.geeksforgeeks.org/largest-element-in-an-array/
"""
def largest_element(arr :list) -> int:
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 0:
            return 0
        max_element = arr[0]
        for x in arr:
            if max_element < x:
                max_element = x
        return max_element
