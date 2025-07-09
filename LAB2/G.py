arrLength, query = map(int, input().split())

arr = list(map(int, input().split()))
def Lregion(arr,target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right )//2        
        
        if arr[mid] < target :
            left = mid + 1 
        else:
            right = mid

    return left

def Rregion(arr,target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right )//2        
        
        if arr[mid] <= target :
            left = mid + 1 
        else:
            right = mid

    return left


for _ in range(query):
    x,y = map(int, input().split())
    
    left = Lregion(arr,x)
    right = Rregion(arr,y)

    print(right - left)

