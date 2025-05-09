Input= input().split()
arr= input().split()
num= int(Input[0])
des= int(Input[1])
if len(arr)==num:
    rev_arr=[]
    for i in range(des):
        rev_arr.append(arr[i])
    for j in range(len(rev_arr)-1,-1,-1):
        print(rev_arr[j],end=" ")