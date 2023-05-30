product = int(input())
num = int(input())

lst = list()
for _ in range(num):
    lst.append(list(map(int, input().split())))

lst.sort()

basic = set(i for i in range(1, product))
for i in lst:
    basic.discard(i[0])


i = 0
while i < len(lst):
    if lst[i][1] not in basic:
        item = lst.pop(i)
        for j in lst:
            if j[0] == item[1]:
                newItem = [item[0], j[1], item[2] * j[2]]
                lst.append(newItem)
    else:
        i += 1

result = list([i, 0] for i in basic)
for i in lst:
    if i[0] == product and i[1] in basic:
        for j in result:
            if j[0] == i[1]:
                j[1] += i[2]
                break

for i in result:
    print(i[0], i[1])