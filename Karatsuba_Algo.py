def karatsuba(x, y):
    # Base case
    if x < 10 or y < 10:
        return x * y

    # Calculate size of numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # 3 recursive calls
    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba((low1 + high1), (low2 + high2)) - z2 - z0

    return (z2 * 10**(2*m)) + (z1 * 10**m) + z0

#https://www.youtube.com/watch?v=yWI2K4jOjFQ&ab_channel=Insidecode