N, M = map(int, input().split())
horseR, horseC, jolR, jolC = map(int, input().split())

map = list(list(9 for _ in range(M+1)) for _ in range(N+1))
map[horseR][horseC] = 0

notGo = list([i, j] for i in range(M) for j in range(N))

def djikstra(nowR, nowC):
    if [nowR, nowC] in notGo:
        notGo.remove([nowR, nowC]) 
    nowMinimum = map[nowR][nowC]
    near = list()
    a, b = 2, 1
    for k in range(2):
        for i in range(2):
            for j in range(2):
                if nowR+a >= 1 and nowR+a <= N and nowC+b >= 1 and nowC+b <= M:
                    near.append([nowR+a, nowC+b])
                    b *= -1
            a *= -1
        a, b = b, a

    for i in near:
            map[i[0]][i[1]] = min(nowMinimum+1, map[i[0]][i[1]])

def minimumNotGo():
    if len(notGo) == 0:
        return 0
    
    minNode = [0, 0]
    minDistance = 100000000
    for i in notGo:
        if minDistance > map[i[0]][i[1]]:
            minDistance = min(minDistance, map[i[0]][i[1]])
            minNode = [i[0], i[1]]
    return minNode

nextNode = [0, 0]
while(nextNode):
    djikstra(horseR, horseC)
    nextNode = minimumNotGo()
    if nextNode != 0:
        horseR = nextNode[0]
        horseC = nextNode[1]

for lst in map:
    print(lst)