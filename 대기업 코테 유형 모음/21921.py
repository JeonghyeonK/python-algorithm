N, X = map(int, input().split())
lst = list(map(int, input().split()))

sum = 0
max_sum = 0
count = 0

if max(lst) == 0:
    print('SAD')
else:
    for i in range(X):
        sum += lst[i]
    max_sum =sum
    count = 1
    
    for i in range(N-X):
        sum = sum-lst[i]+lst[X+i]
        if sum == max_sum:
            count += 1
        elif sum > max_sum:
            max_sum = sum
            count = 1
            
    print(max_sum)
    print(count)