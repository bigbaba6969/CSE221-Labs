def fast():
    a, b = map(int, input().split())
    mod = 107
    
    result = 1
    base = a % mod  
    
    while b > 0:
        if b % 2 == 1:  
            result = (result * base) % mod
        base = (base * base) % mod  
        b //= 2  
    
    print(result)
 
fast()