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

#print(grid)

for k in range(K):

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
            #print(row, col)

            if grid[row][col][0] < grid[min_row][min_col][0]:
                min_row = row
                min_col = col
            elif grid[row][col][0] == grid[min_row][min_col][0]:
                if grid[row][col][1] > grid[min_row][min_col][1]:
                    min_row = row
                    min_col = col
            #print(min_row, min_col)
    grid[min_row][min_col][0] += N + M
    grid[min_row][min_col][1] = k + 1
    #print(grid[min_row][min_col])
    #print("여기까지 가해자")
                
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
            #print(row, col)

            if grid[row][col][0] > grid[max_row][max_col][0]:
                max_row = row
                max_col = col
            elif grid[row][col][0] == grid[max_row][max_col][0]:
                if grid[row][col][1] < grid[max_row][max_col][1]:
                    max_row = row
                    max_col = col
            #print(max_row, max_col)
    #print("여기까지 피해자")

    #최단경로 조사
    visited = deque()
    visited.append([[min_row, min_col]])
    while(len(visited) > 0):
        #print("visited: ", visited)
        route = visited.popleft()
        point = route[-1]
        is_end = False
        #print("point: ",point)
        next_points = [
            [point[0], (point[1]+1)%M],
            [(point[0]+1)%N, point[1]],
            [point[0], (point[1]-1+M)%M],
            [(point[0]-1+N)%N, point[1]]
        ]
        for next_ in next_points:
            if grid[next_[0]][next_[1]][0] == 0:
                #print("zero: ", next_)
                continue

            is_visited = False
            for lst in visited:
                if next_ in lst:
                    is_visited = True
                    break
            if is_visited:
                #print("is visited: ", next_)
                continue
            
            new_route = route.copy()
            new_route.append(next_)
            visited.append(new_route)
            #print("new_route: ", new_route)
            if next_[0] == max_row and next_[1] == max_col:
                #print("end: ", next_)
                is_end = True
                break
        
        if is_end:
            break



    #레이저 공격
    power = grid[min_row][min_col][0]
    if len(visited) > 0:
        # print(k, "th", "before attack")
        # for g in grid:
        #     for h in g:
        #         print(h[0], end=' ')
        #     print()
        # print("route: ", visited[-1])
        # print()
        for i in range(N):
            for j in range(M):
                if grid[i][j][0] <= 0:
                    continue
                if [i, j] in visited[-1]:
                    if i == min_row and j == min_col:
                        continue
                    elif i == max_row and j == max_col:
                        grid[i][j][0] -= power
                    else:
                        grid[i][j][0] -= int(power/2)
                else:
                    grid[i][j][0] += 1

    #포탄 공격
    else:
        row_range = list()
        col_range = list()
        for i in range(-1, 2):
            row_range.append((max_row + i + N) % N)
            col_range.append((max_col + i + M) % M)
        for i in range(N):
            for j in range(M):
                if grid[i][j][0] <= 0:
                    continue
                if i == min_row and j == min_col:
                    continue
                

                if i in row_range and j in col_range:
                    if i == max_row and j == max_col:
                        grid[i][j][0] -= power
                    else:
                        grid[i][j][0] -= int(power/2)

                else:
                    grid[i][j][0] += 1
    
    # print(k, "th", "last")
    # for g in grid:
    #     for h in g:
    #         print(h[0], end=' ')
    #     print()
    # print()

    alive_cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j][0] > 0:
                alive_cnt += 1
        if alive_cnt >= 2:
            break
    if alive_cnt <= 1:
        break

max_power = 0
for i in range(N):
    for j in range(M):
        if grid[i][j][0] > max_power:
            max_power = grid[i][j][0]
print(max_power)


    #레이저 공격
        #상하좌우로 부서진포탑(0) 피해서 이동하는데 가장자리를 통해 반대편 점프 가능
        #최단경로로 공격함, 여러개면 우/하/좌/상 우선순위대로 먼저 움직인 경로 선택
        #최단경로 정해졌으면 공격대상이 공격자의 공격력만큼 수치 피해입음
        #최단경로 위에 있는 포탑도 공격력/2의 몫만큼 공격받음
        #최단경로를 못찾으면 포탄공격

        #최단경로 찾기
            #dq에다가 [row, col] 형식으로 추가
            #dq에서 하나 pop해서 우하좌상으로 하나씩 검사
                #해당 블럭이 0인지
                #해당 블럭까지 도달한 경우가 visited에 있었는지(있었다면 최단이 아님)
            #검사를 통과했다면 dq에 append하기
            #이 과정을 거쳐 목표 포탑이 나오면 끝남. 안나오면 레이저공격 말고 다른공격으로 가야함
            #이때 어떤 경로를 거쳐서 갔는지를 어떻게 저장하지..
            #visited에다가 [[1,1], [1,2], [2,2]] 일케 넣어놓으면 확인 가능하긴 함
            #대신 방문여부 검사시 in vitited 안되고 for _ in visited -> in _ 일케만 가능함

