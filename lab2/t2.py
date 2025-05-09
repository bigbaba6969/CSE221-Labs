def merge_sort(arr1, arr2):
    arr = []  
    i, j = 0, 0  
    n1, n2 = len(arr1), len(arr2)
 
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
 
 
    while i < n1:
        arr.append(arr1[i])
        i += 1
 
 
    while j < n2:
        arr.append(arr2[j])
        j += 1
 
    for i in arr:
        print(i,end=" ")
    
n1=int(input())
inp1=input().split()
arr1=[]
for i in inp1:
    arr1.append(int(i))
n2=int(input())
inp2=input().split()
arr2=[]
for i in inp2:
    arr2.append(int(i))
a=merge_sort(arr1,arr2)