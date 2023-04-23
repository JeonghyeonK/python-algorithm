'''
변수 입력과 연산자
'''


'''
a=input("숫자를 입력하세요 : ")
print(a*2)
'''

'''
띄어쓰기 단위로 입력받음
숫자를 그냥 입력받으면 string형으로 입력됨
a, b=input("숫자를 입력하세요 : ").split()
print(a, b)
print(type(a))
'''

# a, b=input("숫자를 입력하세요 : ").split()
# a=int(a)
# b=int(b)
# print(a+b)

#int로 바로 입력받기, 나눗셈, 몫, 나머지, 거듭제곱 출력
a, b=map(int, input("숫자를 입력하세요 : ").split())
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a=4.3
b=int(input())
c=a+b
print(type(c))