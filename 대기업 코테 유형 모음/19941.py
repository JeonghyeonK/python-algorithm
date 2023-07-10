N, K = map(int, input().split())
str = input()

lastH = -1
result = 0
for i in range(N):
    if str[i] == 'P':
        mostLeft = max(0, i-K, lastH)
        mostRight = min(N-1, i+K)
        for j in range(mostLeft, mostRight+1):
            if str[j] == 'H' and j != lastH:
                lastH = j
                result += 1
                break   

print(result)