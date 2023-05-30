T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    result = (A - B + 3) % 3
    if result == 1:
        print("#", i+1, " A", sep="")
    else:
        print("#", i+1, " B", sep="")
        