'''

다음 명령들 중 하나씩을 Q번 반복함 

    100 - 경주 시작 준비
    P마리 토끼가 (1번~P번) N*M 격자에서 경주 진행할 준비를 함
    i번 토끼의 고유 번호는 pid[i], 이동해야 하는 거리는 d[i]
    처음 토끼들은 모두 1행 1열에 있음
    #rabbits[] : 토끼의 위치를 저장할 list

    200 - 경주 진행
    가장 우선순위 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복함
        우선순위 : 점프 횟수 적은 순 - 서있는 행+열 작은 순 - 행 작은 순 - 열 작은 순 - 고유번호 작은 순
        우선순위 가장 높은 토끼가 i번토끼라 하면 이 토끼가 상하좌우로 d[i]만큼 이동했을때 위치 구함
            이 때 격자 벗어나면 방향 반대로 해서 한 칸 이동
        이렇게 구한 4개의 위치 중 행+열 큰 순 - 행 큰 순 - 열 큰 순으로 우선순위 둬서 가장 우선순위 높은 칸으로 토끼 이동
        이 칸 위치를 (r[i], c[i])라고 했을 때 i번 토끼 제외한 나머지 토끼들은 모두 r[i] + c[i]만큼의 점수를 동시에 얻음
    K번의 턴 진행 후에는 행+열 큰 순 - 행 큰 순 - 열 큰 순으로 우선순위 둬서 가장 우선순위 높은 토끼를 골라 점수 S를 더함
        이 때, K번의 턴 동안 한번이라도 뽑혔던 토끼중에 골라야 함
    #priority_1() : 멀리 보내줄 우선순위 토끼 선정
    #priority_2() : 우선순위 토끼 선정 2
    #next_row_col() : 토끼번호를 넣으면 다음 위치 반환
    #is_picked[] : 뽑혔는지 여부 저장
    #grade[] : 점수 저장
    #jump_cnt[] : 토끼들 점프 횟수

    300 - 이동거리 변경
    고유번호가 pid[t]인 토끼의 이동거리를 L배 해줌.
        이 때 토끼의 이동거리가 10억을 넘어가는 가능성은 없음

    400 - 최고의 토끼 선정
    토끼중 가장 높은 점수를 출력

'''

import sys
input = sys.stdin.readline
import heapq as hq

rabbits = []
grid = []
grade = []
is_picked = []
jump_cnt = []
N, M, P = 0, 0, 0
pid, d = [], []
def priority_1() -> int:
    min_jump, min_row_sum, min_row, min_col, min_pid = 200001, 200001, 100001, 100001, 10000001
    priority_rabbit = 0

    for i in range(len(rabbits)):
        if jump_cnt[i] < min_jump:
            min_jump = jump_cnt[i]
            priority_rabbit = i
        elif jump_cnt[i] == min_jump:
            if rabbits[i][0] + rabbits[i][1] < min_row_sum:
                min_row_sum = rabbits[i][0] + rabbits[i][1]
                priority_rabbit = i
            elif rabbits[i][0] + rabbits[i][1] == min_row_sum:
                if rabbits[i][0] < min_row:
                    min_row = rabbits[i][0]
                    priority_rabbit = i
                elif rabbits[i][0] == min_row:
                    if rabbits[i][1] < min_col:
                        min_col = rabbits[i][1]
                        priority_rabbit = i
                    elif rabbits[i][1] == min_col:
                        if pid[i] < min_pid:
                            min_pid = pid[i]
                            priority_rabbit = i
    return priority_rabbit

def priority_2() -> int:
    max_row_sum, max_row, max_col, max_pid = 0, 0, 0, 0
    priority_rabbit = 0

    for i in len(rabbits):
        if rabbits[i][0] + rabbits[i][1] > max_row_sum:
            max_row_sum = rabbits[i][0] + rabbits[i][1]
            priority_rabbit = i
        elif rabbits[i][0] + rabbits[i][1] == max_row_sum:
            if rabbits[i][0] > max_row:
                max_row = rabbits[i][0]
                priority_rabbit = i
            elif rabbits[i][0] == max_row:
                if rabbits[i][1] > max_col:
                    max_col = rabbits[i][1]
                    priority_rabbit = i
                elif rabbits[i][1] == max_col:
                    if pid[i] > max_pid:
                        max_pid = pid[i]
                        priority_rabbit = i

    return priority_rabbit

def priority_mistake() -> int:
    for summ in range(N+M-2, -1, -1):
        for j in range(M):
            i = summ - j
            if i < 0: break
            if i >= N: continue
            if len(grid[i][j]) == 0: continue

            min_pid = 10000001
            min_pid_rabbit_idx = 9999
            for k in range(len(grid[i][j])):
                if pid[k] < min_pid_idx:
                    min_pid_idx = pid[k]
                    min_pid_rabbit_idx = k

            return min_pid_rabbit_idx


    return 2

def next_row_col(idx: int) -> list():

    now_row, now_col = rabbits[idx][0], rabbits[idx][1]
    next_points = [
        [0, d[idx]],
        [0, -d[idx]],
        [d[idx], 0],
        [-d[idx], 0]
    ]
    next_step_list=[]
    for next_point in next_points:
        next_row = now_row + next_point[0]
        next_col = now_col + next_point[1]
        # while(next_row >= 0 and next_row < N):
        #     if next_row < 0:
        #         next_row -= next_row
        #     elif next_row >= N:
        #         next_row = N-1 - (next_row - N-1)
            
        # while(next_col >= 0 and next_col < M):
        #     if next_col < 0:
        #         next_col -= next_col
        #     elif next_col >= M:
        #         next_col = M-1 - (next_col - M-1)

        # N이 5라서 인덱스 0~4이고 현재는 3이고 d가 20이라고 해보자
        # -방향 : 2 1 0 1 2 3 4 3 2 1 0 1 2 3 4 3 2 1 0 1
        # [0 1 2 3 4 3 2 1] 리스트를 만들어주고
        # 현재 위치 + 방향
        

        # +방향 : 2 3 2 1 0 1 2 3 2 1

        next_step_list.append([next_row, next_col])
    
    max_row_sum, max_row, max_col = 0, 0, 0
    real_next_row_col = []
    for next_step in next_step_list:
        if next_step[0] + next_step[1] > max_row_sum:
            max_row_sum = next_step[0] + next_step[1]
            real_next_row_col = next_step
        elif next_step[0] + next_step[1] == max_row_sum:
            if next_step[0] > max_row:
                max_row = next_step[0]
                real_next_row_col = next_step
            elif next_step[0] == max_row:
                if next_step[1] > max_col:
                    max_col = next_step[1]
                    real_next_row_col = next_step

    return real_next_row_col

 

Q = int(input())
for _ in range(Q):
    command = list(map(int, input().split()))

    if command[0] == 100:
        N, M, P = command[1], command[2], command[3]
        for i in range(4, P*2+4):
            if i%2 == 0:
                pid.append(command[i])
            else:
                d.append(command[i])
        
        rabbits = [[0,0] for _ in range(P)]
        grade = [0 for _ in range(P)]
        is_picked = [False for _ in range(P)]
        jump_cnt = [0 for _ in range(P)]
        grid = [[[] for _ in range(M)] for _ in range(N)]
        grid[0][0] = [i for i in range(P)]

        print(rabbits)
        print("grade", grade)
        print("grid", grid)            
        print(N, M, P)
        print(pid)
        print(d)

    elif command[0] == 200:
        K, S = command[1], command[2]
        print(K, S)

        jumping_rabbit_idx = priority_1()
        his_next_row_col = next_row_col(jumping_rabbit_idx)
        plus_grade = his_next_row_col[0] + his_next_row_col[1]
        for i in range(P):
            if i != jumping_rabbit_idx:
                grade[i] += plus_grade
        is_picked[jumping_rabbit_idx] = True
        jump_cnt[jumping_rabbit_idx] += 1

    elif command[0] == 300:
        pid_t, L = command[1], command[2]
        print(pid_t, L)

    elif command[0] == 400:
        print(400)
