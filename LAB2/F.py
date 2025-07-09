N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
seen = {}  
max_len = 0

for right in range(N):
    elem = arr[right]
    
    if elem in seen:
        seen[elem] += 1
    else:
        seen[elem] = 1

    while len(seen) > K:
        left_elem = arr[left]
        seen[left_elem] -= 1
        if seen[left_elem] == 0:
            del seen[left_elem]  
        left += 1

    
    max_len = max(max_len, right - left + 1)

print(max_len)

