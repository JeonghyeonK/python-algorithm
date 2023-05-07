numList = list()
for i in range(5):
    numList.append(int(input()))  

sum=0
for i in numList:
    if i<40:
        sum+=40
    else:
        sum+=i

print(int(sum/5))