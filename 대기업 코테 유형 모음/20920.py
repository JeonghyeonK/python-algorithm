import sys
N, M = map(int, input().split())

words =  [sys.stdin.readline().strip() for i in range(N)]
frequency = {}
for i in range(N):
    word = words[i]
    if len(word) >= M:  
        if word in frequency.keys():
            frequency[word] += 1
        else:
            frequency[word] = 1

frequency = sorted(frequency.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for i in frequency:
    print(i[0])