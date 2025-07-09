n = int(input())
arr = list(map(int, input().split()))

getmeout = True
while getmeout:

    change = False
    for i in range(n):
        
        if not i == n-1 :
            if arr[i] %2!= 0 and arr[i+1] %2 != 0 or arr[i] %2 == 0 and arr[i+1] %2 ==0:
                
                if arr[i] > arr[i+1] :
                    arr[i], arr[i+1] =  arr[i+1], arr[i]
                    change = True
        
    if change == False:
        getmeout = False
        break

for i in arr:
    print(i, end=(" "))