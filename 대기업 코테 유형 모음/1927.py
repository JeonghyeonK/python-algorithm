import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())

hq = list()
orders = list()
for _ in range(N):
    orders.append(int(input().rstrip()))

for order in orders:
    if order == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, order)
    