N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
sum = 0
max_len = 0

for right in range(N):
    sum += arr[right]
    
    while sum > K:
        sum -= arr[left]
        left += 1

    
    max_len = max(max_len, right - left + 1)

print(max_len)
