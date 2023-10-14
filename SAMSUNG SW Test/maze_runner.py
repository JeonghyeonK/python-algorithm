#포기
# while True:
#     N, M, K = map(int, input().split())

#     miroh = list()
#     miroh.append([0 for _ in range(N+1)])
#     for _ in range(N):
#         miroh.append([0] + list(input().split()))

#     people = list()
#     for _ in range(M):
#         people.append(list(map(int, input().split())))

#     exit = list(map(int, input().split()))

#     print(people)

#     for _ in range(K):
#         for man in people:
#             next_sqaure = man.copy()
#             #print(next_sqaure)
#             if man[0] > exit[0]:
#                 next_sqaure[0] -= 1
#             elif man[0] < exit[0]:
#                 next_sqaure[0] += 1
#             if miroh[next_sqaure[0]][next_sqaure[1]] == 0:
#                 man = next_sqaure.copy()
#                 continue

#             if man[1] > exit[1]:
#                 next_sqaure[1] -= 1
#             elif man[1] < exit[1]:
#                 next_sqaure[1] += 1
#             if miroh[next_sqaure[0]][next_sqaure[1]] == 0:
#                 man = next_sqaure.copy()
#                 continue
#     print(people)
#     break
            
#포기 취소
#재도전        
#미로는 N,N이며, (row, col) 형태
#빈 칸은 0, 벽은 1~9
#입력은 인덱스 1시작 기준으로 받지만 처리는 0시작 기준으로 해주자

#다음을 K번 반복
    #1초마다 모든 참가자는 최단거리가 가까워지는 칸으로 이동
        #최단거리는 x차이 + y차이 라서 그 길에 벽이 있으면 못감
        #선택지가 여러개면 상하로 움직임
            #y축이 가까워지는 칸 -> x축 가까워지는 칸 두개만 검사하면 될듯
        #못움직이면 안움직임
    
    #도달시 탈출

    #미로가 회전함
        #출구와 참가자를 포함하는 가장 작은 정사각형을 잡음
            #선택지가 여러개면 r좌표가 작은 순 - c좌표가 작은 순
        #정사각형이 90도 회전하고, 벽의 내구도 1 감소 -> 0이 되면 벽이 아니게 됨

    #모든 참가자가 탈출하면
        #break

#이동거리 합과 출구 좌표 출력 후 종료
                

'''  
본인 r,c 이동거리 i라고 할 때
    1. (r-i, c-i)~ (r-i, c), (r-i+1, c-i)~ (r, c-i) 검사 -> 이 안에 있으면 시작점[r-i, c-i]

    2. (r-i, c+1)~ (r-i, c+n) 검사 -> 이 안에 있으면 시작점 [r-i, c-i+n]

    3. (r-i+1, c+i) ~ (r, c+i) 검사 -> 이 안에 있으면 시작점 [r-i, c]

    4. (r+n, c-i), (r+n, c+i) 검사 -> 이 안에 있으면 시작점  [r-i+n, c+-i]
        이걸 n이 1부터 i-1까지 반복

    5. (r+i, c-i)~ (r+i, c) 검사 -> 이 안에 있으면 시작점 [r, c-i]

    6. (r+i, c+1)~ (r+i, c+n) 검사 -> 이 안에 있으면 시작점 [r, c-i+n)]
'''



N, M, K = map(int, input().split())
summ = 0
grid = [list(map(int, input().split())) for _ in range(N)]
people = []
for m in range(M):
    man = list(map(int, input().split()))
    people.append([man[0]-1, man[1]-1])
exit = list(map(int, input().split()))
exit = [exit[0]-1, exit[1]-1]

def next_stage(now_point:list()) -> list():
    global summ
    r, c = now_point[0], now_point[1]
    r_next, c_next = r, c
    if exit[0] != r : 
        r_next = r + (exit[0]-r) // abs(exit[0]-r)
    if exit[1] != c:
        c_next = c + (exit[1]-c) // abs(exit[1]-c)
    if grid[r_next][c] == 0:
        summ += 1
        return [r_next, c]
    elif grid[r][c_next] == 0:
        summ += 1
        return [r,c_next]
    else:
        return [r,c]
#만약 사람을 찾아서 사각형을 만들었는데 위나 왼쪽에 마이너스 인덱스가 있으면:

def find_smallest(now_point:list()) -> list():
    r, c = now_point[0], now_point[1]
    new_rc_candi = []
    print("r, c", r, c)
    for i in range(1, N):
        for j in range(i+1):
            if r-i < 0 or c-i < 0: break
            print([r-i, c-i+j], [r-i+j, c-i])
            if [r-i, c-i+j] in people or [r-i+j, c-i] in people:
                return [r-i, c-i, i]
        for j in range(1, i+1):
            if r-i < 0: break
            if c-i+j < 0 or c+j >= N: continue
            print([r-i, c+j])
            if [r-i, c+j] in people:
                return [r-i, c-i+j, i]
        for j in range(1, i+1):
            if c+i >= N: break
            if r-i < 0: continue
            print([r-i+j, c+i])
            if [r-i+j, c+i] in people:
                return [r-i, c, i]
        for j in range(1, i):
            if r-i+j <0 or r+j >= N: continue
            if c-i >= 0 : print([r+j, c-i])
            if c+i < N : print([r+j, c+i])
            if c-i >= 0 and [r+j, c-i] in people:
                return [r-i+j, c-i, i]
            elif c + i < N and [r+j, c+i] in people:
                return [r-i+j, c, i]
        for j in range(i+1):
            if r+i >= N or c-i < 0: break
            print([r+i, c-i+j])
            if [r+i, c-i+j] in people:
                return [r, c-i, i]
        for j in range(1, i+1):
            if r+i >= N : break
            if c-i+j < 0 or c+j >= N: continue
            print([r+i, c+j])
            if [r+i, c+j] in people:
                return [r, c-i+j, i]
        
def rotate(info:list()) :
    r, c, dist = info[0], info[1], info[2]
    square = []
    in_people = []
    in_exit = []
    global exit

# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44


    for i in range(r, r+dist+1):
        square.append(grid[i][c:c+dist+1])
    
    for i in range(dist+1):
        for j in range(dist+1):
            
            if square[i][j] > 0 and square[i][j] <= 9:
                grid[r+j][c+dist-i] = square[i][j] - 1
            elif square[i][j] == 0:
                grid[r+j][c+dist-i] = square[i][j]
            for p in range(len(people)):
                if people[p] == [r+i, r+j]:
                    people[p] = [r+j, c+dist-i]
            if exit == [r+i, c+j]:
                exit = [r+j, c+dist-i]
            



    

    # 00 01 02
    # 10 11 12
    # 20 21 22

    # 20 10 00
    # 21 11 01
    # 22 12 02

    # r값은 i-r이라는 c값이 됨
    # c값은 c라는 r값이 됨
    
for _ in range(K):
    for i in range(len(people)-1, -1, -1):
#        print("people i before: ", people[i])
        people[i] = next_stage(people[i])
#        print("people i after: ", people[i])
        if people[i] == exit:
#            print("pop", i, people[i])
            people.pop(i)
    if len(people) == 0:
        break
    print("exit: ", exit)
    print("people: ", people)
    smallest_square = find_smallest(exit)
    rotate(smallest_square)

print(summ)

