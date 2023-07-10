strs = input()

num = 0
while len(strs)>0:
    num += 1
    numstr = str(num)
    
    for i in range(len(numstr)):
        if strs[0] == numstr[i] :
            strs = strs[1:]
            if len(strs) == 0 :
                break
    
print(num)