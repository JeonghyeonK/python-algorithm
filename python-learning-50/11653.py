import math

N = int(input())

if N!=1:
    for i in range(2, N+1):
        while(N%i==0):
            print(i)
            N/=i