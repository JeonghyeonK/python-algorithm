
'''
기존 버전
a, b, c = map(int, input().split())
lst = [a, b, c]
'''

# 정석
lst = list(map(int, input().split()))

lst.sort()
print(lst[1])