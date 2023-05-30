triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(triangle)

def solution(triangle):
    answer = 0
    
    dp = triangle
    for i in range(1, len(triangle)):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        for j in range(1, len(triangle[i])-1):
            ex1 = triangle[i][j] + dp[i-1][j-1]
            ex2 = triangle[i][j] + dp[i-1][j]
            dp[i][j] = max(ex1, ex2)
        dp[i][len(triangle[i])-1] = triangle[i][len(triangle[i])-1] + dp[i-1][len(triangle[i])-2]
        
    answer = max(dp[-1])
    return answer

solution(triangle)