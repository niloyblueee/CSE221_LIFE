N, M, K = map(int, input().split())

arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split()))

left = 0
right = M-1

output2 = [-1 , -1]
output = []

closest_diff = float("inf")



while left < N and right >= 0:

    if arr1[left] + arr2[right] == K :
        output.append(left+1)
        output.append(right+1)
        break
    
    elif abs(K - (arr1[left] + arr2[right])) < closest_diff :
        closest_diff = abs(K - (arr1[left] + arr2[right]))
        output2 = [left+1 , right+1]

    if arr1[left] + arr2[right] < K :
        left += 1

    else:
        right -= 1

if not output:
    for i in output2:
        print(i, end=(" "))

else:
    for i in output:
        print(i, end=(" "))