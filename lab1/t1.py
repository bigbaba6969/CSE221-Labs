
inp= int(input())
list1=[]
for i in range(inp):
    num= int(input())
    list1.append(num)
for j in list1:
    if j%2==0:
        print(f"{j} is an Even number.")
    else:
        print(f"{j} is an Odd number.")