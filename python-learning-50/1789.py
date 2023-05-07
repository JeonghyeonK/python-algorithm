import math

S = int(input())

N = int(math.sqrt(S*2))
if N*(N+1)/2 > S:
    N-=1

print(N)