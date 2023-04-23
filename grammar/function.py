'''
함수 만들기
'''

# def add(a, b):
#     c=a+b
#     return c

# x=add(3, 2)
# print(x)

# 튜플 형태로 리턴하는 함수
def add(a, b):
    c=a+b
    d=a-b
    return c, d

print(add(5, 3))


def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')