def quicksort(arr):
    """In-place quicksort for a list of integers.
    Steps:
    1. Choose a pivot (last element).
    2. Partition the array into elements ≤ pivot and > pivot.
    3. Recursively sort the partitions.
    """

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1] # swap pivot to correct position
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

"""
| Case    | Time Complexity | Explanation                                     |
| ------- | --------------- | ----------------------------------------------- |
| Best    | `O(n log n)`    | Pivot always splits the array evenly            |
| Average | `O(n log n)`    | Random pivot or average-case splits             |
| Worst   | `O(n²)`         | Pivot always picks the smallest/largest element |

Space: O(log n) for recursion (in-place algorithm)

In-place, unstable, fastest in practice

"""