N = int(input())
lst = list()
original = input()
for _ in range(N-1):
    lst.append(input())

result = 0

for i in range(N-1):
    
    if abs(len(original) - len(lst[i])) >1:
        continue
        
    originalCount = {}
    lstCount = {}
    for j in range(len(original)):
        if original[j] not in originalCount.keys():
            originalCount[original[j]] = 1
        else:
            originalCount[original[j]] += 1
    for j in range(len(lst[i])):
        if lst[i][j] not in lstCount.keys():
            lstCount[lst[i][j]] = 1
        else:
            lstCount[lst[i][j]] += 1
    
    for j in originalCount:
        if j in lstCount:
            lstCount[j] -= originalCount[j]
            originalCount[j] = 0
    
    difference = 0
    for j in originalCount:
        difference += abs(originalCount[j])
    for j in lstCount:
        difference += abs(lstCount[j])
    
    if difference <= 2:
        result += 1
        
        
            
            
print(result)