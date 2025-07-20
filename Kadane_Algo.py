def max_subarray_sum_with_subarray(arr):
    if not arr:
        return 0, [] # Return sum 0 and an empty list for an empty array

    max_so_far = arr[0]
    current_max = arr[0]

    # Indices for the current maximum subarray ending at `i`
    current_start = 0
    current_end = 0 

    # Indices for the overall maximum subarray found so far
    max_start = 0
    max_end = 0

    for i in range(1, len(arr)):
        # If starting a new subarray from arr[i] is better than extending the current one
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
            current_start = i # New subarray starts here
            current_end = i   # And ends here initially
        else:
            # Continue the current subarray
            current_max = current_max + arr[i]
            current_end = i   # Extend the end of the current subarray

        # If the current_max is greater than the overall max_so_far
        if current_max > max_so_far:
            max_so_far = current_max
            max_start = current_start
            max_end = current_end

    # Handle the case where all numbers are negative
    # If the largest sum is a single negative number (e.g., in [-5, -1, -3])
    # the above logic correctly handles this as current_max and max_so_far 
    # would be initialized with arr[0] and then updated if a less negative 
    # single element is found.
    
    # Extract the actual subarray using the stored indices
    actual_subarray = arr[max_start : max_end + 1] 

    return max_so_far, actual_subarray

# --- Example Usage ---
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum1, sub1 = max_subarray_sum_with_subarray(arr1)
print(f"Array: {arr1}")
print(f"Max Sum: {sum1}, Subarray: {sub1}") # Expected: Max Sum: 6, Subarray: [4, -1, 2, 1]
print("-" * 30)

arr2 = [1, 2, 3, -2, 5]
sum2, sub2 = max_subarray_sum_with_subarray(arr2)
print(f"Array: {arr2}")
print(f"Max Sum: {sum2}, Subarray: {sub2}") # Expected: Max Sum: 9, Subarray: [1, 2, 3, -2, 5]
print("-" * 30)

arr3 = [-1, -2, -3, -4]
sum3, sub3 = max_subarray_sum_with_subarray(arr3)
print(f"Array: {arr3}")
print(f"Max Sum: {sum3}, Subarray: {sub3}") # Expected: Max Sum: -1, Subarray: [-1]
print("-" * 30)

arr4 = [5]
sum4, sub4 = max_subarray_sum_with_subarray(arr4)
print(f"Array: {arr4}")
print(f"Max Sum: {sum4}, Subarray: {sub4}") # Expected: Max Sum: 5, Subarray: [5]
print("-" * 30)

arr5 = []
sum5, sub5 = max_subarray_sum_with_subarray(arr5)
print(f"Array: {arr5}")
print(f"Max Sum: {sum5}, Subarray: {sub5}") # Expected: Max Sum: 0, Subarray: []
print("-" * 30)

arr6 = [-2, -3, 4, -1, -2, 1, 5, -3]
sum6, sub6 = max_subarray_sum_with_subarray(arr6)
print(f"Array: {arr6}")
print(f"Max Sum: {sum6}, Subarray: {sub6}") # Expected: Max Sum: 7, Subarray: [4, -1, -2, 1, 5]