MOD = 107           

def power_mod(a, b) :
    res  = 1               
    base = a % MOD          
    while b:              
        if b & 1:         
            res = (res * base) % MOD   
        base = (base * base) % MOD    
        b >>= 1             
    return res

a,b = map(int,input().split())
print(power_mod(a,b))