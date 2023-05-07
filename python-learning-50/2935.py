A=input()
operator=input()
B=input()

ALen = len(A)
BLen = len(B)
maxLen=max(ALen, BLen)
isAEqualB = (ALen == BLen)
answer= ''

if operator=='*':
    answer+='1'
    for i in range(ALen+BLen-2):
        answer+='0'
    
elif operator=='+' :
    if ALen == BLen:
        answer +='2'
        for i in range(maxLen-1):
            answer+='0'
    else:
        for i in range(maxLen, 0, -1):
            if i == ALen:
                answer+='1'
            elif i == BLen:
                answer+='1'
            else:
                answer+='0'

print(answer)   