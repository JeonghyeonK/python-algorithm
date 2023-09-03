N = int(input())

bigger_list = list(map(int, input().split()))

people_list = [N for _ in range(N)]

for i in range(N):
    position = 0
    
    
    for _ in range(bigger_list[i]):
        while(people_list[position] < i):
            position += 1
        position += 1
        
    while(people_list[position] < i):
        position += 1
    people_list[position] = i

for p in people_list:
    print(p+1, end=' ')


'''
1번친구는 자신의 위치를 바로 알 수 있음
2번친구는 자신보다 키 큰 사람의 위치와 1번친구의 위치 고려해 알 수 있음

bigger_list에서 0부터 N-1까지 돎
매 반복마다:


'''