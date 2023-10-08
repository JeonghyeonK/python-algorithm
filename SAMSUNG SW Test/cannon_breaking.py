# N*M 리스트 필요

#다음을 K번 반복
    #공격자(가장 약한 포탑) 선정
        #공격력이 가장 낮은 포탑이 유일하면 걔로 선정
        #여러개면 가장 최근에 공격한 포탑을 선정
            #이거때문에 리스트 원소에 공격 시점 적어야함
        #여러개면 행+열값 큰 거 선정 -> 여러개면 열값 기준

        #그러니까..
        #4,4 - 3,4 - 4,3 - 2,4 - 3,3 - 이런 순으로 행+열 우선순위대로 공격력을 검사함
        #새로운 최소값이 나오면 min_val이 본인이 되고
        #동률값이 나오면 공격시점 비교해서 업데이트

    #선정된 포탑에 공격력 N+M만큼 더함
    #공격받을자(가장 강한 포탑) 선정
        #공격력이 가장 높은 포탑이 유일하면 걔로 선정
        #여러개면 가장 옛날에 공격한 포탑을 선정
        #여러개면 행+열값 작은 거 선정 -> 여러개면 열값 기준
    #레이저 공격 시도 후 안되면 포탄 공격함
    #레이저 공격
        #상하좌우로 부서진포탑(0) 피해서 이동하는데 가장자리를 통해 반대편 점프 가능
        #최단경로로 공격함, 여러개면 우/하/좌/상 우선순위대로 먼저 움직인 경로 선택
        #최단경로 정해졌으면 공격대상이 공격자의 공격력만큼 수치 피해입음
        #최단경로 위에 있는 포탑도 공격력/2의 몫만큼 공격받음
        #최단경로를 못찾으면 포탄공격
    #포탄 공격
        #공격 대상은 공격자의 공격력만큼 수치 피해 입음
        #주위 8개의 포탑도 공격자 공격력/2의 몫만큼 피해 입음
        #공격자는 영향받지 않음
        #가장자리에 포탄 떨어지면 반대편 점프해서 피해줌
    #포탑 부서짐
        #공격력 0이하면 부서짐
    #포탑 정비
        #부서지지 않은 포탑 중 공격자와 피해자(절반피해 포함) 아닌 포탑은 +1됨
        #공격한 포탑 최근 공격으로 업데이트

#0이 아닌 포탑이 1개 뿐이면 중지
#K번 반복이 끝나면 중지
#남아있는 포탑 중 가장 강한 포탑의 공격력을 출력하면 프로그램 종료


from collections import deque

#입력받기
N, M, K = map(int, input().split())
grid = list()
for _ in range(N):
    col = list(map(int, input().split()))
    for i in range(M):
        col[i] = [col[i], 0]
    grid.append(col)

print(grid)


#공격자 선정
min_row = -1
min_col = -1
for i in range(N+M-2, -1, -1):
    for col in range(M-1, -1, -1):
        row = i - col

        if row >= N:
            break
        elif row < 0:
            continue
        if grid[row][col][0] <= 0:
            continue
        if min_row == -1:
            min_row = row
            min_col = col
            continue
        print(row, col)

        if grid[row][col][0] < grid[min_row][min_col][0]:
            min_row = row
            min_col = col
        elif grid[row][col][0] == grid[min_row][min_col][0]:
            if grid[row][col][1] > grid[min_row][min_col][1]:
                min_row = row
                min_col = col
        print(min_row, min_col)
grid[min_row][min_col][0] += N+M
print(grid[min_row][min_col])

print("여기까지 가해자")
            
#피해자 선정
max_row = -1
max_col = -1

for i in range(0, N+M-1):
    for col in range(0, M):
        row = i - col
        if row >= N:
            continue
        elif row < 0:
            break
        if grid[row][col][0] <= 0:
            continue
        if row == min_row and col == min_col:
            continue
        if max_row == -1:
            max_row = row
            max_col = col
            continue
        print(row, col)

        if grid[row][col][0] > grid[max_row][max_col][0]:
            max_row = row
            max_col = col
        elif grid[row][col][0] == grid[max_row][max_col][0]:
            if grid[row][col][1] < grid[max_row][max_col][1]:
                max_row = row
                max_col = col
        print(max_row, max_col)

print("여기까지 피해자")

bfs = deque()
visited = set()
bfs.append([[min_row, min_col]])
while(len(bfs) > 0):
    point = bfs.popleft()
    print(point)
    next_points = [
        [point[0][0], point[0][1]+1],
        [point[0][0]+1, point[0][1]],
        [point[0][0], point[0][1]-1],
        [point[0][0]-1, point[0][1]]
    ]
    for next_ in next_points:
        if grid[next_[0]][next_[1]][0] > 0:
            bfs.append(point.append(next_))
    print(bfs)
    break


    #레이저 공격
        #상하좌우로 부서진포탑(0) 피해서 이동하는데 가장자리를 통해 반대편 점프 가능
        #최단경로로 공격함, 여러개면 우/하/좌/상 우선순위대로 먼저 움직인 경로 선택
        #최단경로 정해졌으면 공격대상이 공격자의 공격력만큼 수치 피해입음
        #최단경로 위에 있는 포탑도 공격력/2의 몫만큼 공격받음
        #최단경로를 못찾으면 포탄공격