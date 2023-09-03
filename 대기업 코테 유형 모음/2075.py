import sys
import heapq

input = sys.stdin.readline

N = int(input())
n_num = [x+1000000000 for x in list(map(int, input().split()))]
heapq.heapify(n_num)

for i in range(N-1):
    new_n_num = list(map(int, input().split()))
    for i in range(N):
        heapq.heappushpop(n_num, new_n_num[i]+1000000000)

answer = heapq.heappop(n_num) - 1000000000
print(answer)



'''
처음 N개짜리 받아서 리스트 만듦
다음 N개짜리를 받아서 리스트에 pushpop하는 것을 N-1번 반복
만들어진 리스트에서 가장 작은 수 배출


'''