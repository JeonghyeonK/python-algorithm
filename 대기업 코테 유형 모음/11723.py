import sys

lst = set()
T = int(input())

for i in range(T):
    oprAndNum = sys.stdin.readline().strip().split()
    if len(oprAndNum) == 1:
        if oprAndNum[0] == 'all':
            lst.clear()
            for j in range(1, 21):
                lst.add(j)
        elif oprAndNum[0] == 'empty':
            lst.clear()
    else:
        oprAndNum[1] = int(oprAndNum[1])
        if oprAndNum[0] == 'check':
            print(1) if oprAndNum[1] in lst else print(0)
        elif oprAndNum[0] == 'toggle':
            lst.discard(oprAndNum[1]) if oprAndNum[1] in lst else lst.add(oprAndNum[1])
        elif oprAndNum[0] == 'add':
            lst.add(oprAndNum[1])
        elif oprAndNum[0] == 'remove':
            lst.discard(oprAndNum[1])