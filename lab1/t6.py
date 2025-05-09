def min_swaps(n,ids, marks):
    students=[]
    for i in range(n):
        stu= (ids[i], marks[i])
        students.append(stu)
    count= 0
    for i in range(n):
        max= i
        for j in range(i + 1, n):
            if (students[j][1]==students[max][1] and students[j][0]<students[max][0]) or (students[j][1]>students[max][1]):
                max= j
 
        if max!= i:
            students[i], students[max]=students[max], students[i]
            count+= 1
 
    print(f"Minimum swaps: {count}")
    for student in students:
        print(f"ID: {student[0]} Mark: {student[1]}")
 
n = int(input())
student_ids = input().split()
mark = input().split()
ids=[]
marks=[]
for i in student_ids:
    ids.append(int(i))
for j in mark:
    marks.append(int(j))
 
 
 
min_swaps(n, ids, marks)