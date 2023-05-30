board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0],[0,0,1,0],[0,0,1,0]]

def solution(board):
    answer = 1234
    
    col = len(board)
    row = len(board[0])
    dp = [[0 for _ in range(row+1)] for _ in range(col+1)]
    print(dp)
    
    for i in range(col):
        for j in range(row):
            if board[i][j] == 1:
                dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
            
    
    print(dp)
    answer = 0
    for i in range(col+1): 
        for j in range(row+1):
            answer = max(answer, dp[i][j])
            
    answer **= 2
    print(answer)
    return answer

solution(board)