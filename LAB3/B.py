def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_arr, left_cnt = mergesort(arr[:mid])
    right_arr, right_cnt = mergesort(arr[mid:])

    
    right_squares = sorted([x ** 2 for x in right_arr])

    
    cross_cnt = 0
    for val in left_arr:
        cross_cnt += count_less_than(right_squares, val)

    
    merged = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])

    return merged, left_cnt + right_cnt + cross_cnt



def count_less_than(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low  


N = int(input())
arr = list(map(int, input().split()))

_, result = mergesort(arr)
print(result)
