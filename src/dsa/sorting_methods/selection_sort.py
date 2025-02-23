def selection_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


a = [7, 6, 5, 4, 3, 2, 1]
print(selection_sort(a))
