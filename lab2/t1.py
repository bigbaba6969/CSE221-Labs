n = input().split()
l = int(n[0])
sum_target = int(n[1])
inp = input().split()
arr = []
for i in inp:
    arr.append(int(i))
 
if l == len(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        cur_sum = arr[i] + arr[j]
        if cur_sum == sum_target:
            print(i + 1, j + 1) 
            break
        elif cur_sum > sum_target:
            j -= 1
        else:
            i += 1
    else:
        print(-1)  
else:
    print(-1) 