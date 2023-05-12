N = int(input())
lst = list(map(int, input().split()))
M = int(input())

low = 0
high = max(lst)
mid = (low+high)//2

while(True):
    sum = 0
    for i in lst:
        if i <= mid:
            sum += i
        else:
            sum += mid
    if sum > M:
        high = mid
    else:
        low = mid
    mid = (low+high)//2
    
    if high-low == 1:
        sum = 0
        for i in lst:
            if i <= high:
                sum += i
            else:
                sum += high
        if sum > M:   
            print(low)
        else:
            print(high)
        break