def max_squared_sum(arr):
    max_val = float('-inf')
    max_so_far = arr[0] 
    
    for j in range(1, len(arr)):
        max_val = max(max_val, max_so_far + arr[j] ** 2)
        max_so_far = max(max_so_far, arr[j]) 
    
    return max_val
 
 
n = int(input())
arr = list(map(int, input().split()))
 
 
result = max_squared_sum(arr)
 
 
print(result)