N, M = map(int, input().split())
NMList = list()
wayList = list()
for _ in range(N):
    NMList.append(list(map(int, input().split())))
    wayList.append([[]]*M)

sumList = NMList.copy()

print(NMList)
print(wayList)
    
for n in range(1, N):
    for m in range(0, M):
        sumList[n][m] = sumList[n-1][m] + NMList[n][m]
        wayList[n][m] = ['under']
        
        if m>0:
            newnum = sumList[n-1][m-1] + NMList[n][m]
            print(newnum, sumList[n][m])
            if newnum < sumList[n][m]:
                sumList[n][m] = newnum
                wayList[n][m] = ['left']
            elif newnum == sumList[n][m]:
                wayList.append('left')
                print('ff')
                
            
            
        if m < M-1:
            newnum = sumList[n-1][m+1] + NMList[n][m]
            if newnum < sumList[n][m]:
                sumList[n][m] = newnum
                wayList[n][m] = ['right']
            elif newnum == sumList[n][m]:
                wayList.append('right')
        

print(sumList)
print(NMList)
print(wayList)