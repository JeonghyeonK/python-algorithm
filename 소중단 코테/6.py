num, cnt = map(int, input().split())

n = cnt
lst = list()
while (n > 0):
    if n % 2 == 1:
        lst.append(1)
        n //= 2
    else:
        lst.append(0)
        n //= 2

lst2 = list()
for i in range(len(lst)):
    lst2.append(num)
    num *= num

result = 1
for i in range(len(lst)):
    if lst[i] == 1:
        result *= lst2[i]
    
print(result%20091024)