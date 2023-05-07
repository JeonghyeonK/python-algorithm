T = int(input())

for i in range(T):
    list = input().split(' ')
    
    num = float(list[0])
    list = list[1:]
    
    for j in list:
        if j=='@':
            num*=3
        elif j=='%':
            num+=5
        elif j=='#':
            num-=7
    print(format(num, ".2f"))