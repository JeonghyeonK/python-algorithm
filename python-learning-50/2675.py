T = int(input())

for i in range(T):
    list = input().split()
    
    num = int(list[0])
    newStr = ''
    for i in range(len(list[1])):
        for j in range(num):
            newStr+=list[1][i]
            
    print(newStr)