N = int(input())
lst = list()

for i in range(N):
    lst.append([i]+list(map(int, input().split()))+[1])

lst.sort(key= lambda x : (x[1], x[2]), reverse=True)

for i in range(N):
    for j in range(i):
        if lst[j][1]>lst[i][1] and lst[j][2]>lst[i][2] :
            lst[i][3] += 1

lst.sort(key= lambda x : x[0])

for i in lst:
    print(i[3], end=' ')