import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = dict()
result = N
for _ in range(N):
    keywords[input().rstrip()] = 1

for _ in range(M):
    usedWords = sorted(input().rstrip().split(","))
    
    for word in usedWords:
        if word in keywords.keys():
            if keywords[word] == 1:
                keywords[word] = 0
                result -= 1
    
    print(result)