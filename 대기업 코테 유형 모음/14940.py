import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

target_map = list()
distance_map = [[n*m for _ in range(m)] for _ in range(n)]
#print(distance_map)
for _ in range(n):
    line = list(map(int, input().split()))
    target_map.append(line)
    
target = [n, m]
for i in range(n):
    for j in range(m):
        if target_map[i][j] == 2:
            target[0] = i
            target[1] = j
            distance_map[i][j] = 0
        elif target_map[i][j] == 0:
            distance_map[i][j] = 0

bfs = deque()
bfs.append(target)
while(len(bfs) > 0):
    point = bfs.popleft()
    
    # point 주변 4개의 점들 중 1인 점을 deque에 추가
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i+j not in [-1, 1]:
                continue
            new_point = [point[0]+i, point[1]+j]
            if new_point[0] < 0 or new_point[0] >= n or new_point[1] < 0 or new_point[1] >= m:
                continue
            if target_map[new_point[0]][new_point[1]] == 0:
                continue
            if distance_map[point[0]][point[1]] + 1 < distance_map[new_point[0]][new_point[1]]:
                distance_map[new_point[0]][new_point[1]] = distance_map[point[0]][point[1]] + 1
                bfs.append([new_point[0], new_point[1]])
    

for i in range(n):
    for j in range(m):
        if distance_map[i][j] == n*m:
            distance_map[i][j] = -1

for lst in distance_map:
    for distance in lst:
        print(distance, end=' ')
    print()



'''
target부터 시작
deque에서 포인트 한 개 꺼내서
포인트 주변 8개 점 탐색
지도를 나가거나, 포인트가 0이면 제외하고
1인 지점은 deque에 추가

deque 길이 0이면 종료
'''