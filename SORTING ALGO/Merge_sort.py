def mergesort(arr):
    """Stable merge sort for a list of integers.
    Steps:
    1. Divide the array into halves recursively.
    2. Merge the sorted halves back together.
    3. Repeat until the entire array is sorted.
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = mergesort(arr)
print("Sorted array:", sorted_arr)

"""
| Case    | Time Complexity | Explanation                                     |
| ------- | --------------- | ----------------------------------------------- |
| Best    | `O(n log n)`    | Merging halves consistently takes linear time   |
| Average | `O(n log n)`    | Merging halves consistently takes linear time 
| Worst   | `O(n log n)`    | Merging halves consistently takes linear time   |


Space: O(n) for temporary arrays (not in-place)

Stable, preferred for linked lists

"""