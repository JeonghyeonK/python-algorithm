#n*n 격자가 있음
#사람 m명이 각각 자기 번호대로 1~m분에 각자의 베이스캠프에서 출발해 편의점으로 이동하기 시작
    #출발 전에는 격자 밖에 있음
    #각자의 목표 편의점은 모두 다름

#매 1분마다 이루어지는 일
    #격자에 있는 사람들 모두 본인 최애 편의점 쪽으로 1칸 움직임
        #최단거리로 움직이며, 여러가지일 경우 상좌우하 우선순위로 움직임
    #만약 편의점에 도착한다면 이동 종료
        #해당 편의점은 다른 사람들이 지나갈 수 없게 됨
        #단, 격자 사람들이 모두 이동한 뒤에 지나갈 수 없게 바뀌는 것임
    #매 분 t번 사람은 t분에 본인 최애 편의점과 최단거리인 베이스캠프에 들어감
        #최단거리가 여러개면 행이 작은 곳, 행이 같으면 열이 작은 곳으로 들어감
        #베이스캠프로 이동하는 데에는 시간소요 x
        #해당 베이스캠프는 다른 사람들이 지나갈 수 없게 됨
        #단, 격자 사람들이 모두 이동한 뒤에 지나갈 수 없게 바뀌는 것임

#몇분 후에 도착하는지 구하기

from collections import deque 

n, m = map(int, input().split())
basecamps = list(list(map(int, input().split())) for _ in range(n))
stores = list(list(map(int, input().split())) for _ in range(m))
people = [None]
t = 1 

def shortest_next_step(sp:list, ep:list) -> list():
    visited = list()
    come = list([None for _ in range(n)] for _ in range(n))
    dq = deque()
    shift_list = [
        [-1, 0],
        [0, -1],
        [0, 1],
        [1, 0]
    ]
    dq.append(sp)
    visited.append(sp)

    while(len(dq)>0):
        step = dq.popleft()
        for shift in shift_list:
            ny, nx = step[0] + shift[0], step[1] + shift[1]
            if min(ny, nx) < 0 or max(ny, nx) >= n: continue

            #다음 위치가 안가본 곳이고 갈 수 있는 곳이면
            if [ny, nx] not in visited and basecamps[ny][nx] >= 0: # 수정 필요
                dq.append([ny, nx])
                visited.append([ny, nx])
                come[ny][nx] = step

            #다음 위치가 내가 찾던 그곳이면
            if ny == ep[0] and nx == ep[1]:
                before_step = ep
                while True:
                    if come[before_step[0]][before_step[1]] == sp:
                        break
                    before_step = come[before_step[0]][before_step[1]]
                return before_step

def shortest_basecamp(sp:list) -> list():
    for distance in range(1, n*2-2):
        for i in range(sp[0]-distance, sp[0]+distance+1):
            #격자 바깥 제외해주고
            if i < 0 or i >= n: continue
            if distance - abs(sp[0]-i) == 0:
                if basecamps[i][sp[1]] == 1:
                    return [i, sp[1]]
            else:
                for j in [sp[1] - (distance - abs(sp[0]-i)), sp[1] + (distance - abs(sp[0]-i))]:
                    if j < 0 or j >= n: continue
                    if basecamps[i][j] == 1:
                        return [i, j]
    return list()
        

#매 1분마다 이루어지는 일
for i in range(t+1):
    new_ban_list = list()

    #격자에 있는 사람들 모두 본인 최애 편의점 쪽으로 1칸 움직임
        #최단거리로 움직이며, 여러가지일 경우 상좌우하 우선순위로 움직임
    for i in range(1, t):
        if people[i] == stores[i]:
            continue
        people[i] = shortest_next_step(people[i], stores[i])

    #만약 편의점에 도착한다면 이동 종료
        #해당 편의점은 다른 사람들이 지나갈 수 없게 됨
        #단, 격자 사람들이 모두 이동한 뒤에 지나갈 수 없게 바뀌는 것임
        if people[i] == stores[i]:
            new_ban_list.append[stores]

    #매 분 t번 사람은 t분에 본인 최애 편의점과 최단거리인 베이스캠프에 들어감
        #최단거리가 여러개면 위에꺼, 높이 같으면 왼쪽꺼로 들어감
        #베이스캠프로 이동하는 데에는 시간소요 x
        #해당 베이스캠프는 다른 사람들이 지나갈 수 없게 됨
        #단, 격자 사람들이 모두 이동한 뒤에 지나갈 수 없게 바뀌는 것임
        people.append(shortest_basecamp(stores[i]))
        new_ban_list.append[people[t]]

    for ban in new_ban_list:
        basecamps[ban[0]][ban[1]] = -1
    


# print(shortest_next_step([1,2], [3,4]))
# print(basecamps)
# print(stores)
# print(shortest_basecamp([3,3]))


