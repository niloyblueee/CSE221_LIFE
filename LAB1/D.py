
t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = "YES"
    for j in range(n):
        if arr[j] != arr[-1]:    
            if arr[j] > arr[j+1]:
                flag = "NO"
                break    
    print(flag)