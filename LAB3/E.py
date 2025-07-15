def mod_pow(a, n, m):
    res = 1
    while n:
        if n & 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res

def mod_sum(a, n, m):
    if a == 1:
        return n % m
    if n == 1:
        return a % m
    if n % 2 == 0:
        half = mod_sum(a, n // 2, m)
        a_half = mod_pow(a, n // 2, m)
        return (half + a_half * half) % m
    else:
        return (mod_sum(a, n - 1, m) + mod_pow(a, n, m)) % m

T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(mod_sum(a, n, m))
