def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        check=False
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                check=True
        if check==False:
            break
 
n=int(input())
num=input().split()
arr=[]
if len(num)==n:
    for i in num:
        arr.append(int(i))
bubbleSort(arr)
for i in arr:
    print(i,end=" ")