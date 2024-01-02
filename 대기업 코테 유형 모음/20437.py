from collections import deque

T = int(input())

for t in range(T):
    strr = input()
    num = int(input())
    
    maxNum = 0
    minNum = 10001
    cntList = [deque() for i in range(26)]
    for idx in range(len(strr)):
        letter = ord(strr[idx]) - 97
        cntList[letter].append(idx)
        
        if len(cntList[letter]) == num:
            newNum = cntList[letter][num-1] - cntList[letter][0] + 1
            cntList[letter].popleft()
            maxNum = max(maxNum, newNum)
            minNum = min(minNum, newNum)
        
    if minNum == 10001:
        print(-1)
    else:
        print(minNum, maxNum)