n = int(input())

answer = 0

dp = [1] + [0] * n
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
    dp[i] = dp[i-2]+dp[i-1]
answer = dp[n]
print(answer)
