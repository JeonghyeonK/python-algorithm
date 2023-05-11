A, B = input().split()

interval = len(B)-len(A)
lst = list()
min_interval=len(B)

for i in range(0, interval+1):
    new_interval = 0
    for j in range(len(A)):
        if B[j+i] != A[j]:
            new_interval+=1
    min_interval = min(min_interval, new_interval)

print(min_interval) 
