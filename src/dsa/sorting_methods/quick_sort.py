def quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)  # Sort left partition
        quick_sort_inplace(arr, pivot_index + 1, high) # Sort right partition

def partition(arr, low, high):
    pivot = arr[high]  # Choosing last element as pivot
    i = low - 1  # Pointer for smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1

# Example usage
a = [7, 6, 5, 4, 3, 2, 1]
quick_sort_inplace(a, 0, len(a) - 1)
print(a)