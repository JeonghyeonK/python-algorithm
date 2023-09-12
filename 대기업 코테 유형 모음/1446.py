N, D = map(int, input().split())
shortcut_dict = dict()
for _ in range(N):
    start, end, leng = map(int, input().split())
    if end in shortcut_dict.keys():
        shortcut_dict[end].append([start, leng])
    else:
        shortcut_dict[end] = [[start, leng]]
dp = [i for i in range(D+1)]
for i in range(1, D+1):
    if i not in shortcut_dict.keys():
        dp[i] = dp[i-1] + 1
    else:
        for shortcut in shortcut_dict[i]:
            #print(shortcut)
            dp[i] = min(dp[i], dp[i-1] + 1, dp[shortcut[0]] + shortcut[1])

print(dp[D])