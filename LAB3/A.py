
def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0 

    mid = len(arr) // 2
    left, inv_left = mergesort(arr[:mid])
    right, inv_right = mergesort(arr[mid:])
    merged , inv = merge(left, right)
    return merged, inv_left + inv_right + inv

def merge(left, right):
    merged = []
    i = j = inv=  0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv
    
N = int(input())
arr = list(map(int, input().split()))
arr, inv = mergesort(arr)
print(inv)
print(*arr)