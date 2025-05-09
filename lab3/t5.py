def find_bst_insertion_order(arr):
    arr.sort() 
    result = []
 
    def insert_order(start, end):
        if start > end:
            return
        mid = (start + end) // 2
        result.append(arr[mid])  
        insert_order(start, mid - 1)  
        insert_order(mid + 1, end)  
    insert_order(0, len(arr) - 1)
    return result
 
 
n = int(input())
arr = list(map(int, input().split()))
 
 
if len(arr) != n:
    print("Error: Number of elements does not match n")
 
else:
    result = find_bst_insertion_order(arr)
    print(" ".join(map(str, result)))