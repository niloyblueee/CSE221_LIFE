def build(arr, result):
    if not arr:
        return
    mid = len(arr) // 2
    result.append(arr[mid])  # root
    build(arr[:mid], result)  # left
    build(arr[mid+1:], result)  # right

n = int(input())
arr = list(map(int, input().split()))
result = []
build(arr, result)
print(*result)
