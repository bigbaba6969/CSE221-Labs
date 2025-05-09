import sys
 
def mod_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
 
def geometric_sum(a, n, m):
    if a == 1:
        return n % m  
 
    num = mod_exponentiation(a, n + 1, m * (a - 1)) - a  
    den = a - 1  
    
    return (num // den) % m  
 
def main():
    sys.stdin = open(0)
    input = sys.stdin.read
    data = input().split("\n")
 
    T = int(data[0]) 
    results = []
 
    for i in range(1, T + 1):
        if not data[i].strip():
            continue
        a, n, m = map(int, data[i].split())
        results.append(str(geometric_sum(a, n, m)))
 
    print("\n".join(results))
 
if __name__ == "__main__":
    main()
