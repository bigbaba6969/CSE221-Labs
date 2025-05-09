Input=int(input())
list1=[]
for i in range(Input):
    Calcu=input().split()
    char=Calcu[0]
    no1=int(Calcu[1]) 
    sign=Calcu[2]
    no2=int(Calcu[3])
    if sign=='+':
        sum=str(no1 + no2)+ ".000000"
        list1.append(sum)
    elif sign=='-':
        sum=str(no1 - no2)+".000000"
        list1.append(sum)
    elif sign=='*':
        sum=str(no1 * no2)+".000000"
        list1.append(sum)
    elif sign=='/':
        sum=str(no1 / no2)+"00000"
        list1.append(sum)
for i in list1:
    print(i)