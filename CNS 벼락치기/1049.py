N, M = map(int, input().split())

set_min = 1001
EA_min = 1001
total = 0

for _ in range(M):
    set_price, EA_price = map(int, input().split())
    set_min = min(set_min, set_price)
    EA_min = min(EA_min, EA_price)
    
remain = N%6

if set_min > EA_min * 6:
    total = N * EA_min
elif remain * EA_min < set_min:
    total = (N//6) * set_min +remain * EA_min
else:
    total = (N//6 + 1) * set_min
    
print(total)