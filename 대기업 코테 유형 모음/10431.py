T = int(input())
for i in range(T):
    lst = list(map(int, input().split()))
    num = lst[0]
    del lst[0]
    new_lst = list()
    steps=0
    
    for j in lst:
        new_lst.append(j)
        new_lst.sort()
        steps+=len(new_lst) - new_lst.index(j)-1
    
    print(num, steps)