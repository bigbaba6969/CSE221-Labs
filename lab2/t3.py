def longest_subarray(N, K, arr):
    left = 0
    max_length = 0
    current_sum = 0
 
    for right in range(N):
        current_sum += arr[right]
 
        while current_sum > K:
            current_sum -= arr[left]
            left += 1
 
        max_length = max(max_length, right - left + 1)
 
    print(max_length)
 
 
N, K = map(int, input().split())
arr = list(map(int, input().split()))
longest_subarray(N, K, arr)  