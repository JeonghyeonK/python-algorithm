
num = int(input())
lst = list(map(int, input().split()))
professor, jogyo = map(int, input().split())

result = 0
for i in lst:
    i = i - professor
    result += 1 
    if i <= 0:
        continue
    else:
        result += i // jogyo
    if i % jogyo != 0:
        result += 1
        
print(result)