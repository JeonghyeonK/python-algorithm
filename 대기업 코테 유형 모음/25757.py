set1=set()
N, G = input().split()
N=int(N)
if G == 'Y':
    G = 1
elif G == 'F':
    G = 2
elif G == 'O':
    G = 3
    

for _ in range(N):
    set1.add(input())

print(int(len(set1)/G)) 