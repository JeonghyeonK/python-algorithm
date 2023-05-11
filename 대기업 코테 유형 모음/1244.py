n = int(input())
lst = list(map(int, input().split()))
std_num = int(input())
students = list()
for _ in range(std_num):
    students.append(list(map(int, input().split())))
    
for student in students:
    if student[0] == 1:
        for i in range(student[1]-1, n, student[1]):
            if lst[i] == 0:
                lst[i] = 1 
            else:
                lst[i] = 0
    else:
        center = student[1]-1
        for i in range(min(center+1, n-center)):
            if lst[center-i] == lst[center+i]:
                if lst[center-i] == 0:
                    lst[center-i] = lst[center+i] = 1 
                else:
                    lst[center-i] = lst[center+i] = 0
            else:
                break

for i in range(n):
    if i%20==19:
        print(lst[i])
    else:
        print(lst[i], end=' ')