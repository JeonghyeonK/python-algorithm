n = int(input())
m = list( map(int, input().split(' ')))
 
for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])
    
print(max(m))

# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# num_list = list(map(int, input().split()))

# pnm = deque()
# max_num = -1001

# for i in num_list:
#     if max_num <= 0:
#         max_num = max(max_num, i)
    
#     if len(pnm) == 0:
#         pnm.append(i)
#     elif pnm[-1] * i >=0:
#         pnm[-1] += i
#     else:
#         pnm.append(i)

# print(pnm)

# if max_num <= 0:
#     print(max_num)
# else:
#     for i in range(len(pnm) - 2):
#         if pnm[i] <= 0:
#             continue
#         if pnm[i] >= -pnm[i+1] and pnm[i+2] >= -pnm[i+1]:
#             pnm[i+2] = pnm[i] + pnm[i+1] + pnm[i+2]
#             i += 1

#     print(pnm)
#     print(max(pnm))