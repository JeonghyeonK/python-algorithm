N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
spot = list()

min_price = 1000000001
for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
        spot.append([i, min_price])
spot.append([N-1, 0])

total = 0
for i in range(len(spot)-1):
    between = 0
    for j in range(spot[i][0], spot[i+1][0]):
        between += distance[j]
    total += between * spot[i][1]

print(total)
        
