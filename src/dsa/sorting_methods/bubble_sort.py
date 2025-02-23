def bubble_sort(arr: list) -> list:
    list_length = len(arr)
    for i in range(list_length):
        swap = 0
        for j in range(0, list_length - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = 1
            print(arr)
        if swap == 0:
            break
    return arr


a = [7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(a))
