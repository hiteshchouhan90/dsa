"""
https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays

Given two sorted arrays arr1[] and arr2[] of size N and M respectively. The task is to find the union of the two arrays.

Union of two sorted arrays means to find all the unique elements in both the arrays.

Example 1:

Input:
arr1[] = {1,2,3,2,1}
arr2[] = {2,1,2,3,1}
Output: 1 2 3
Explanation: 1, 2 and 3 are present in both
the arrays.
Example 2:

Input:
arr1[] = {2,1,2,2,1}
arr2[] = {2,2,1,2}
Output: 1 2 
"""
def sorted_union(arr1: list, arr2: list) -> list:
    i = 0
    j = 0
    final_list = []
    prev = None
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j] and arr1[i] != prev:
            final_list.append(arr1[i])
            prev = arr1[i]
            i += 1
        elif arr1[i] < arr2[j] and arr1[i] == prev:
            i += 1
        elif arr1[i] > arr2[j] and arr2[j] != prev:
            final_list.append(arr2[j])
            prev = arr2[j]
            j += 1
        elif arr1[i] > arr2[j] and arr2[j] == prev:
            j += 1
        elif arr1[i] == arr2[j] and arr1[i] != prev:
            final_list.append(arr1[i])
            prev = arr1[i]
            i += 1
            j += 1
        elif arr1[i] == arr2[j] and arr1[i] == prev:
            i += 1
            j += 1
    while i < len(arr1):
        if arr1[i] != prev:
            final_list.append(arr1[i])
            prev = arr1[i]
        i += 1
    while j < len(arr2):
        if arr2[j] != prev:
            final_list.append(arr2[j])
            prev = arr2[j]
        j += 1
    return final_list

if __name__ == "__main__":
    arr1 = [1,2,2,3,4]
    arr2 = [5,6,6,7,7]
    print(sorted_union(arr1, arr2))