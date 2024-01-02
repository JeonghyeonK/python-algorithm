leng = int(input())
lst = list(map(int, input().split()))

start = 0
answer = 0
dct = dict()

for end in range(len(lst)):
    if lst[end] not in dct.keys():
        dct[lst[end]] = end
        #print(dct)
    else:
        start = max(start, dct[lst[end]] + 1)
        dct[lst[end]] = end
        #print(dct)
    answer += end - start + 1
    #print(start, end, answer)
    
print(answer)
