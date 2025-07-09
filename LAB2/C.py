n, target1 = map(int, input().split())
a = list(map(int, input().split()))


arr = [(a[i], i+1) for i in range(n)]
arr.sort()  

for i in range(n):
    target = target1 - arr[i][0]
    left = i + 1
    right = n - 1

    while left < right:
        sum_leftright = arr[left][0] + arr[right][0]
        if sum_leftright == target:
            print(arr[i][1], arr[left][1], arr[right][1])
            exit()
        elif sum_leftright < target:
            left += 1
        else:
            right -= 1


print(-1)
