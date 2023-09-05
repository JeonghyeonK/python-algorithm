from collections import deque

N, K = map(int, input().split())

sequence = list(map(int, input().split()))


num_dict = dict()
num_update_dict = dict()
max_length = 0
length = 0
start_point = 0
for i in range(len(sequence)):
    if sequence[i] not in num_dict.keys():
        num_dict[sequence[i]] = deque()
        num_dict[sequence[i]].append(i)
        length += 1
        #print(length, max_length, num_dict)
        continue
    if len(num_dict[sequence[i]]) == K:
        max_length = max(max_length, length)
        num_dict[sequence[i]].append(i)
        last_idx = num_dict[sequence[i]].popleft()
        start_point = max(start_point, last_idx)
        length = i - start_point
        
    else:
        num_dict[sequence[i]].append(i)
        length += 1
    #print(length, max_length, num_dict)
    
max_length = max(max_length, length)
print(max_length)