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

"""
| Iteration | left                             | right | mid | not\_divisible = mid - mid//x | k reached? | action                                         | answer |
| --------- | -------------------------------- | ----- | --- | ----------------------------- | ---------- | ---------------------------------------------- | ------ |
| 1         | 1                                | 14    | 7   | 7 − 2 = 5                     | 5 < 7      | move **left = mid + 1** ⇒ 8                    | 0      |
| 2         | 8                                | 14    | 11  | 11 − 3 = 8                    | 8 ≥ 7      | **answer = 11**, move **right = mid − 1** ⇒ 10 | 11     |
| 3         | 8                                | 10    | 9   | 9 − 3 = 6                     | 6 < 7      | left = 10                                      | 11     |
| 4         | 10                               | 10    | 10  | 10 − 3 = 7                    | 7 ≥ 7      | **answer = 10**, right = 9                     | 10     |
| stop      | left = 10, right = 9 → loop ends |       |     |                               |            |                                                | **10** |

"""