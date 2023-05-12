import math

N = int(input())
M = int(input())
x = list(map(int, input().split()))

first_load = x[0] - 0
last_load = N - x[M-1]
min_height = max(first_load, last_load)

if N>=2:
    for i in range(1, M):
        min_height = max(min_height, math.ceil((x[i]-x[i-1])/2))

print(min_height)