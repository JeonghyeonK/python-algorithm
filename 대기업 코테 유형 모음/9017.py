T = int(input())

for _ in range(T):
    
    num = int(input())
    lst = list(map(int, input().split()))
    
    team_num = max(lst)
    
    team_list = list()
    for i in range(team_num):
        team_list.append([0, 0, 0, 0])
    
    for i in range(num):
        team_list[lst[i]-1][0] += 1
        if team_list[lst[i]-1][0] == 5:
            team_list[lst[i]-1][2] = i
        
    personal_score = 1
    for i in range(num):
        if team_list[lst[i]-1][0]==6 and team_list[lst[i]-1][3] < 4:
            team_list[lst[i]-1][1] += personal_score
            personal_score += 1
            team_list[lst[i]-1][3] += 1
    
    least_score = 10000
    winner = 0
    for i in range(num):
        if team_list[lst[i]-1][0] == 6:
            if least_score > team_list[lst[i]-1][1]:
                winner = i
                least_score = team_list[lst[i]-1][1]
            elif least_score == team_list[lst[i]-1][1] and team_list[lst[i]-1][2] < team_list[lst[winner]-1][2]:
                winner = i
                least_score = team_list[lst[i]-1][1]
                
        
    print(team_list)
    print(winner + 1)