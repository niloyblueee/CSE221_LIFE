_ = list(map(int,input().split()))
length = _[0]
target = _[1]
arr = list(map(int,input().split()))

left = 0 
right = length - 1

while left < right : 
    #print(f"{left} {right}")
    if arr[left] + arr[right] == target:
        print(f"{left+1} {right+1}")
        break
    elif arr[left] + arr[right] > target:
        right -= 1 

    else:
        left +=1

else:
    print("-1")