def rec_bubble_sort(arr: list, n: int = None) -> list:
    if n is None:
        n = len(arr)

    if n == 1:  # Base case, this means array is sorted
        return arr

    # perform one round of bubble sorting
    swapped = False
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            swapped = True

    # if no swaps were made, the array is already sorted
    if not swapped:
        return arr

    return rec_bubble_sort(arr, n - 1)


a = [7, 6, 5, 4, 3, 2, 1]

print(rec_bubble_sort(a))

