def karatsuba(x, y):
    """
    Implements the Karatsuba algorithm for multiplying two integers.
    """
    if x < 10 or y < 10:
        return x * y

    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split the numbers into two halves
    a = x // (10**m)
    b = x % (10**m)
    c = y // (10**m)
    d = y % (10**m)

    """Can also be donee with divmod()
       a, b = divmod(x, 10**m)
       c, d = divmod(y, 10**m)"""

    # Recursively calculate the three products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results
    return ac * (10**(2 * m)) + ad_plus_bc * (10**m) + bd 

if __name__ == "__main__":
    # Example usage
    num1 = 1234
    num2 = 5678
    result = karatsuba(num1, num2)
    print(f"The product of {num1} and {num2} using Karatsuba is: {result}")
    print(f"Verification using standard multiplication: {num1 * num2}")

    num3 = 987654321
    num4 = 123456789
    result2 = karatsuba(num3, num4)
    print(f"\nThe product of {num3} and {num4} using Karatsuba is: {result2}")
    print(f"Verification using standard multiplication: {num3 * num4}")

#https://youtu.be/yWI2K4jOjFQ?si=HMwb494OPdNVbl8k&t=284