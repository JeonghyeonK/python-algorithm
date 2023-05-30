strs = input()

num = 0
while len(strs)>0:
    num += 1
    if strs[0] in str(num) :
        
        strs = strs[1:]
        
        
        
    
print(num)