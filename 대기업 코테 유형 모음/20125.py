N = int(input())
lst = list()
head = False
heart = [0, 0]
body = [0, 0, 0, 0, 0]

for i in range(N):
    lst.append(input())
    if head == False:
        if '*' in lst[i]:
            head = lst[i].index('*')
            heart = [i+2, head+1]
    else:
        if body[0] == 0 and '*' in lst[i]:
            arm_start, arm_end = 0, 0
            if lst[i][0] == '*':
                arm_start = 0
            for j in range(1, N):
                if lst[i][j-1] == '_' and lst[i][j] == '*':
                    arm_start = j
                elif lst[i][j-1] == '*' and lst[i][j] == '_':
                    arm_end = j-1
                elif lst[i][j] == '*' and j == N - 1:
                    arm_end = j
            body[0] = head-arm_start
            body[1] = arm_end-head
        elif body[0]!=0 and lst[i].count('*') == 1:
            if body[3] == 0:
                body[2] += 1
            else:
                if lst[i][head-1] == '*':
                    body[3] += 1
                else:
                    body[4] += 1
        elif body[0]!=0 and lst[i].count('*') == 2:
            body[3] += 1
            body[4] += 1

print(heart[0], heart[1])
for i in range(5):
    print(body[i], end=' ')