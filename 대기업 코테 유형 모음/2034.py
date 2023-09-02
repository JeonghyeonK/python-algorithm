N = int(input())
pillar_list = list()
for _ in range(N):
    pillar = list(map(int, input().split()))
    pillar_list.append(pillar)
    
pillar_list.sort()

vertex_list = list()
vertex_list_reverse = list()

#print(pillar_list)

max_height = 0
for i in range(N):
    if pillar_list[i][1] > max_height:
        vertex_list.append(pillar_list[i])
        max_height = pillar_list[i][1]

max_height = 0
for i in range(N-1, -1, -1):
    if pillar_list[i][1] > max_height:
        vertex_list_reverse.append([pillar_list[i][0]+1, pillar_list[i][1]])
        max_height = pillar_list[i][1]

vertex_list_reverse.sort()
for vertex in vertex_list_reverse:
    vertex_list.append(vertex)

#print(vertex_list)

answer = 0
for i in range(len(vertex_list)-1):
    height = min(vertex_list[i][1], vertex_list[i+1][1])
    answer += height * (vertex_list[i+1][0] - vertex_list[i][0])
    #print(height * (vertex_list[i+1][0] - vertex_list[i][0]))

print(answer)