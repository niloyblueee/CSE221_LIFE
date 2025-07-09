def find_not_divisible(k, x):
    if x == 1:
        return k
    left = 1
    right = 2 * k 
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        not_divisible = mid - (mid // x)
        
        if not_divisible >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


query = int(input())
for _ in range(query):
    k, x = map(int, input().split())
    print(find_not_divisible(k, x))
