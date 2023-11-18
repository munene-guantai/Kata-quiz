def find_unsorted_subarray(arr):
    n = len(arr)


    if n <= 1:
        return [0, 0]


    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    
    if left == n - 1:
        return [0, 0]


    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1


    subarray_min = min(arr[left:right + 1])
    subarray_max = max(arr[left:right + 1])

    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1

    while right < n - 1 and arr[right + 1] < subarray_max:
        right += 1

    return [left, right]

arr = [5, 4, 3, 2, 8, 7, 6]
result = find_unsorted_subarray(arr)
print(result)