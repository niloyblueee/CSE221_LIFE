def counting_sort_cumulative(arr):
    """
    Stable counting sort for a list of *non‑negative* integers.
    Steps:
    1. Build frequency array.
    2. Convert to cumulative (prefix‑sum) array.
    3. Traverse input from right to left, placing items into their
       final positions in the output array.
    """

    if not arr:
        return []

    # ---------- 1. Frequency array ----------
    max_val = max(arr)
    freq = [0] * (max_val + 1)          # freq[i] = how many times i appears
    for num in arr:
        freq[num] += 1

    # ---------- 2. Cumulative / prefix‑sum array ----------
    # After this loop, cum[i] tells us how many elements are ≤ i.
    
    cum = freq[:]                        # copy so original freq is preserved (optional)
    for i in range(1, len(cum)):
        cum[i] += cum[i - 1]

    # ---------- 3. Build the sorted output ----------

    output = [0] * len(arr)

    for num in reversed(arr):            # reverse for stability
        cum[num] -= 1                    # last index where `num` should go
        output[cum[num]] = num           # place `num` in the output array
    
    return output

# Example usage:
nums = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort_cumulative(nums))    # ➜ [1, 2, 2, 3, 3, 4, 8]



"""
| Case    | Time Complexity | Explanation                                          |
| ------- | --------------- | ---------------------------------------------------- |
| Best    | `O(n + k)`      | `k` = max value in array                             |
| Average | `O(n + k)`      | Efficient for small range of integers                |
| Worst   | `O(n + k)`      | Becomes inefficient when `k` is much larger than `n` |

Space: O(k) for the count array
	Only for small range of non-negative integers

"""