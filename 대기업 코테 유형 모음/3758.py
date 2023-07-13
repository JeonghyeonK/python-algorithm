T = int(input())
for _ in range(T):
    
    n, k, t, m = map(int, input().split())
    lst = list()
    submitOrder = list()
    for _ in range(n+1):
        lst.append([0] * (k+1))
    for _ in range(m):
        i, j, s = map(int, input().split())
        lst[i][j] = max(lst[i][j], s)
        lst[i][0] += 1
        if i in submitOrder:
            submitOrder.remove(i)
        submitOrder.append(i)
    
    sumList = list()
    for i in range(1, len(lst)):
        sum = 0
        for j in range(1, len(lst[i])):
            sum += lst[i][j]
        sumList.append([i, sum, lst[i][0], submitOrder.index(i)])
    
    sumList.sort(key = lambda x : (-x[1], x[2], x[3]))
    for i in range(n):
        if sumList[i][0] == t:
            print(i+1)