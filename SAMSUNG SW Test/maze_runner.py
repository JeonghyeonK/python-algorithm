#포기

N, M, K = map(int, input().split())

miroh = list()
miroh.append([0 for _ in range(N+1)])
for _ in range(N):
    miroh.append([0] + list(input().split()))

people = list()
for _ in range(M):
    people.append(list(map(int, input().split())))

exit = list(map(int, input().split()))

print(people)

for _ in range(K):
    for man in people:
        next_sqaure = man.copy()
        #print(next_sqaure)
        if man[0] > exit[0]:
            next_sqaure[0] -= 1
        elif man[0] < exit[0]:
            next_sqaure[0] += 1
        if miroh[next_sqaure[0]][next_sqaure[1]] == 0:
            man = next_sqaure.copy()
            continue

        if man[1] > exit[1]:
            next_sqaure[1] -= 1
        elif man[1] < exit[1]:
            next_sqaure[1] += 1
        if miroh[next_sqaure[0]][next_sqaure[1]] == 0:
            man = next_sqaure.copy()
            continue
print(people)
            
        
