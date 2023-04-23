'''
리스트와 내장함수
'''

import random as r

a=[]
# print(a)
b=list()
# print(b)

a=[1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b=list(range(1, 11))
# print(b)

c=a+b
# print(c)

# 맨 뒤에 6 추가
a.append(6)
# print(a)

#맨 뒤 요소 삭제
a.pop()
# print(a)

# 3번 인덱스에 7 끼워넣기
a.insert(3, 7)
# print(a)

# 3번 인덱스 요소 삭제
a.pop(3)
# print(a)

# 4라는 값을 가진 첫번째 요소 제거
a.remove(4)
# print(a)

# 5라는 값을 가진 첫번째 요소의 인덱스 번호 출력
# print(a.index(5))

a=list(range(1, 11))
# print(a)

# 리스트의 합, 최대값, 인자값들 중 최소값 출력
# print(sum(a))
# print(max(a))
# print(min(7, 5))

# 리스트 무작위로 섞기
r.shuffle(a)
# print(a) 

# 내림차순, 오름차순, 리스트 비우기
a.sort(reverse=True)
# print(a) 
a.sort()
# print(a)
a.clear
# print(a)

# a=[23, 12, 36, 53, 19]
# print(a)
# print(a[:3])
# print(a[1:4])

# 홀수만 출력
for x in a:
    if x%2==1:
        print(x, end=' ')
# print()

# 튜플은 리스트와 달리 변경 불가, 소괄호로 씀
b=(1, 2, 3, 4, 5)
# print(b[0])

# 튜플 형태로 출력. ex) (0, 23), (1, 12) ..
for x in enumerate(a):
    print(x)
print()

for index, value in enumerate(a):
    print(index, value)

# all 함수 : 모든 요소가 참이면 참을 반환, 하나라도 거짓이면 거짓을 반환
if all(50>x for x in a):
    print("Yes")
else:
    print("No")

# any 함수 : 어느 요소가 참이면 참을 반환, 모두 거짓이면 거짓을 반환
if any(15>x for x in a):
    print("Yes")
else:
    print("No")