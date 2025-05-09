def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= right:
        temp.append(arr[j])
        j += 1
    
    for i in range(len(temp)):
        arr[left + i] = temp[i]
    
    return inv_count
 
def merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort(arr, left, mid)
        inv_count += merge_sort(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)
    return inv_count
 
 
n = int(input())
arr = list(map(int, input().split()))
 
inversions = merge_sort(arr, 0, n - 1)
 
 
print(inversions)
print(*arr)