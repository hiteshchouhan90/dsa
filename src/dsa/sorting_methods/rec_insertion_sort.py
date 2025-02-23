def rec_insertion_sort(arr: list, n: int = None) -> list:
    if n is None:
        n = len(arr)
    #base case
    if n <=1:
        return arr
    
    rec_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:  # Compare with the last element
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last   # Place the last element in its correct position   

    return arr


a = [7, 6, 5, 4, 3, 2, 1]
print(rec_insertion_sort(a))        # Output: [1, 2, 3, 4, 5, 6, 7]
print(rec_insertion_sort([3, 1, 2]))  # Output: [1, 2, 3]    # Output: [1, 2, 3]
print(rec_insertion_sort([1]))        # Output: [1]         # Output: [1]
