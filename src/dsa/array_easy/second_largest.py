"""Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

https://www.geeksforgeeks.org/second-largest-element-in-an-array/"""

def second_largest(arr: list) -> int:
    if len(arr) < 2:
        return -1
    largest = arr[0]
    second_largest = -1
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x != largest and x > second_largest:
            second_largest = x
    return second_largest