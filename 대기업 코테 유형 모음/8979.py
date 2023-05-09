N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
    

print(lst)
lst.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)
print(lst)

idx = [lst[i][0] for i in range(N)].index(K)
for i in range(N):
    if lst[idx][1:] == lst[i][1:]:
        print(i+1)
        break 