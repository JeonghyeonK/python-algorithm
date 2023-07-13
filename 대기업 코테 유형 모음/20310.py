S = input()
newS = ""

sum0, sum1 = 0, 0
for i in S:
    if i == '0':
        sum0 += 1
    elif i == '1':
        sum1 += 1

half0 = sum0 / 2
half1 = sum1 / 2
count0 = 0
count1 = 0
for i in S:
    if i == "0":
        if count0 < half0:
            newS = newS + "0"
            count0 += 1
    elif i == "1":
        if count1 < half1:
            count1 += 1
        else:
            newS = newS + "1"
print(newS)