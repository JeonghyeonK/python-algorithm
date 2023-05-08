str = input().upper()
lst = list(set(str))
    
cnt=list()

for i in lst:
    cnt.append(str.count(i))
    
if cnt.count(max(cnt))>1:
    print('?')
else:
    print(lst[cnt.index(max(cnt))])