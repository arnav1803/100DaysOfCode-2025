def dutch_national_flag_sort(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

arr = [2, 0, 1, 2, 1, 0, 0]
sorted_arr = dutch_national_flag_sort(arr)
print("Sorted array:", sorted_arr)
