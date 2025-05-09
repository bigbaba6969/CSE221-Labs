T = int(input())
list1=[]
for _ in range(T):
    N = int(input())
    sum = (N*(N+1))/2
    list1.append(sum)
for i in list1:
    print(int(i))