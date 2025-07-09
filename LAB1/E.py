n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)

evens = sorted(arr[::2])
odds = sorted(arr[1::2])

sorted_even = sorted(sort_arr[ : : 2])
sorted_odd = sorted(sort_arr[ 1 : : 2])


if evens == sorted_even and odds == sorted_odd:
    print("YES")
else:
    print("NO")