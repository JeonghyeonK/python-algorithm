import sys

input = sys.stdin.readline

p, m = map(int, input().split())


all_room_list = list()
for _ in range(p):
    
    l, n = input().split()
    l = int(l)
    new_user = [l, n]
    
    for room in all_room_list:
        if len(room) < m:
            if room[0][0] <= l+10 and room[0][0] >= l-10:
                room.append(new_user)
                l = -1
                break
    if l != -1:
        new_room = list()
        new_room.append(new_user)
        all_room_list.append(new_room)
    
        
for room in all_room_list:
    room.sort(key = lambda x : x[1])
    if(len(room) == m):
        print("Started!")
    else:
        print("Waiting!")
    for user in room:
        print(user[0], user[1])
            





# 한 방을 하나의 list, 멤버를 list 내 요소로 함
# 모든 방을 담을 전체 방 list도 있음, 
# dict형식으로 레벨 - 닉네임으로 받음
# 전체 방 list에서 앞에서부터 입장 가능 레벨 탐색 후 입장 가능하면 들어감