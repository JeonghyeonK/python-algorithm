# 세상 쉬운 문제였음
t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])


'''
T = int(input())

answer = 0
def dfs(n):
    global step
    for i in range(1, n):
        now = (i + 2) % 3
        before1 = (i + 1) % 3
        before2 = i % 3 
        step[now] = [step[before1][0], step[before1][1] + step[before2][4], step[before1][2] + step[before2][5], step[before1][3] + step[before2][6], step[before1][4], step[before1][5] + step[before1][6], step[now][6]]
        
        
for i in range(T):
    n = int(input())
    if n == 0:
        print(1)
        continue
    
    step = [[1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0, 1]]
    now = (n + 2) % 3
    answer = 0
    dfs(n)
    for j in range(7):
        answer += step[now][j]
    
    
    
    print(answer, step)

'''