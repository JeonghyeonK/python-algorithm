A, B, C = map(int, input().split())
D = int(input())

C+=D
while C>=60:
    C-=60
    B+=1
while B>=60:
    B-=60
    A+=1
    A%=24

print(A, B, C)