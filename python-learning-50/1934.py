T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    a=max(A,B)
    b=min(A,B)
    
    while b!=0:
        a%=b
        a, b = b, a
    
    print(A*B//a)