import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dq = deque()

for _ in range(N):
    dq.append(int(input()))

sliding_window = dict()
max_sushi = 0
for i in range(k):
    if dq[i] not in sliding_window.keys():
        sliding_window[dq[i]] = 1
    else:
        sliding_window[dq[i]] += 1
if c not in sliding_window.keys():
    max_sushi = len(sliding_window.keys()) + 1
else:
    max_sushi = len(sliding_window.keys())

#print(sliding_window)

for i in range(N):
    removed_sushi = dq[i]
    added_sushi = dq[(i+k)%N]
    
    if sliding_window[removed_sushi] <= 1:
        sliding_window.pop(removed_sushi)
    else:
        sliding_window[removed_sushi] -= 1
    
    if added_sushi not in sliding_window.keys():
        sliding_window[added_sushi] = 1
    else:
        sliding_window[added_sushi] += 1
        
    if c not in sliding_window.keys():  
        kind_of_sushi = len(sliding_window.keys()) + 1
    else:
        kind_of_sushi = len(sliding_window.keys())
    max_sushi = max(max_sushi, kind_of_sushi)
    
    #print(kind_of_sushi, sliding_window)

print(max_sushi)


'''
deque에 초밥 삼만개 받기
딕셔너리에 초밥종류 : 개수 dq0~dq2999에 대해 넣기
dq0~dq2999부터 시작점, 끝점 둘다 1씩 증가하며 딕셔너리 개수 조정
맥스값이랑 비교 후 업데이트
'''