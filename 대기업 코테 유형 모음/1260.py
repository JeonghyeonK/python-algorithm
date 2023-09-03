import sys 
from collections import deque 
input = sys.stdin.readline


    

N, M, V = map(int, input().split())

graph = dict()

# 그래프 입력받기
for _ in range(M):
    v1, v2 = map(int, input().split())
    if v1 not in graph.keys():
        graph[v1] = set([v2])
    else:
        graph[v1].add(v2)
    if v2 not in graph.keys():
        graph[v2] = set([v1])
    else:
        graph[v2].add(v1)

# DFS

visited = set()

def dfs(root):
    print(root, end=' ')
    visited.add(root)
    if root in graph.keys():
        child_list = sorted(list(graph[root]))
        for child in child_list:
            if child not in visited:
                dfs(child)
    return(root)

dfs(V)
print()
    


# BFS

visited = set()
dq = deque()

dq.append(V)
visited.add(V)

while(len(dq) > 0):
    print(dq[0], end=' ')
    parent = dq.popleft()
    if parent in graph.keys():
        child_list = sorted(list(graph[parent]))
        
        
        for child in child_list:
            if child not in visited:
                dq.append(child)
                visited.add(child)
'''

deque에 1번 입장
1 프린트, visited에 들어감
자식 중 visited에 없는 2, 3, 4 입장
2 프린트, visited에 들어감
2의 자식 중 visited에 없는 자식들 입장
이걸 deque 길이가 0이 될 때 까지?

'''