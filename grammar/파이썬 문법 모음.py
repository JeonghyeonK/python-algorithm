import heapq
from sys import maxsize
import sys

#숫자 여러개 input
N, K = map(int, input().split())

# input 많이 할 때
input = sys.stdin.readline
input = sys.stdin.readline().strip().split #공백 제거하고 띄어쓰기단위로 입력

# heapq
lst = [3, 5, 8, 2, 4]
heapq.heapify(lst)
print(lst)
heapq.heappush(lst, maxsize) # 정수 최댓값
heapq.heappush(lst, 0)
print(lst)
heapq.heappop(lst) # 가장 작은 원소 추출
print(lst)

#set
#set은 중복을 제거해주지만, 순서 보장을 하지 않음
#따라서 정렬 필요시 list에 담아서 sort 돌려야 됨
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7])
#교집합, 합집합, 차집합
print("intersection", s1&s2)
print("union", s1|s2)
print("difference", s1 - s2)

s1.add(0)
s1.discard(0)
s1.remove(1) # 값 못찾으면 오류
s1.pop() # 맨 앞에서 pop, 원소 없으면 오류
print(s1)

#딕셔너리
fruit = {}
fruit = dict()
fruit = {
 	'count':4, 
    'country':'Korea', 
    'season':'Summer', 
    'types':['watermelon', 'mesil', 'koreanMelon', 'peach']
}
print("keys", list(fruit.keys()))
print("values", list(fruit.values()))
print("items", list(fruit.items()))
if 'capital' not in fruit:
    fruit['capital'] = "seoul"
print("new items", list(fruit.items()))


dict = open("dict.txt", 'r')
for line in dict:
    print(line)
    break
dict.close()

#deque
from collections import deque

que = deque()
for i in range(1, 7):
    que.append(i)

for _ in range(2):
    que.popleft()
    que.append(que.popleft())
print(que[0])
que.reverse()
que2 = deque()
que2.append(3)
que.extend(que2)
print("que", que)


# 문자열
msg="It is Time"
tmp=msg.upper()
print(tmp.find('T'))
print(tmp.count('T'))
print(msg[3:5])    
# 소문자 알파벳만 출력
for x in msg:
    if x.islower():
        print(x, end=' ')
# 알파벳만 출력
for x in msg:
    if x.isalpha():
        print(x, end='')
# 아스키 코드 출력
tmp='AZ'
for x in tmp:
    print(ord(x))
    print(ord(x))
# 반대로 출력
tmp=66
print(chr(tmp))

# for문이 break에 걸리지 않고 종료되면 else문 실행
for i in range(1,11):
    if i>15:
        break
else:
    print(20) 
    


#list와 tuple

import random as r
a=[]
a=list()

# 빈 list
emptyList = [None] * 5
emptyList = [[] for _ in range(5)]

# list 얕은 복사
emptyList = a.copy()

a=[1, 2, 3, 4, 5]
# 맨 뒤에 6 추가
a.append(6)
#맨 뒤 요소 삭제
a.pop()
# 3번 인덱스에 7 끼워넣기
a.insert(3, 7)
# 3번 인덱스 요소 삭제
a.pop(3)
# 4라는 값을 가진 첫번째 요소 제거
a.remove(4)
# 2라는 값을 가진 첫번째 요소의 인덱스 번호 출력
print("index2", a.index(2))
a=list(range(1, 11))
# print(sum(a))
# print(max(a))

# 리스트 무작위로 섞기
r.shuffle(a)

del a[0] # 삭제

# 내림차순, 오름차순, 리스트 비우기
a.sort(reverse=True)
a.clear

lst = [[2, 1], [3, 4], [1, 3], [2, 0]]
lst.sort(key= lambda x : (x[0], x[1]))
print("sorted", lst)

# 튜플은 리스트와 달리 변경 불가, 소괄호로 씀
b=(1, 2, 3, 4, 5)

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
    
plus_two=lambda x: x+2
print(plus_two(1))

# map : 인자가 두 개인데, 앞은 함수고 뒤는 자료
def plus_one(x):
    return x+1
a=[1, 2, 3]
print(list(map(plus_one, a)))   
# 위와 같은 로직, 익명함수를 통해 간결해짐
print(list(map(lambda x: x+1, a)))


import math

print(math.ceil(2.5))
print(math.floor(2.5))

# 함수 안에 함수 만들고 참조하기
def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
    B()
    print(x)      # A의 지역 변수 x 출력
A()

# 다시 시작