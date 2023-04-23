'''
람다 함수
'''


# print(plus_one(1))

plus_two=lambda x: x+2
print(plus_two(1))

# map : 인자가 두 개인데, 앞은 함수고 뒤는 자료
def plus_one(x):
    return x+1
a=[1, 2, 3]
print(list(map(plus_one, a)))   

# 위와 같은 로직, 익명함수를 통해 간결해짐
print(list(map(lambda x: x+1, a)))

