# 한 줄 주석은 #, 여러줄 주석은 ' 세 개

'''
# 변수명 정하기
# 영문과 숫자, _로 이루어짐
# 대소문자를 구분
# 문자나 _로 시작
# 특수문자 비허용
# 키워드(예약어) 사용 금지

'''

a=1
A=2
c=5
print(a, A, c)

a, b, c  = 3, 2, 1
print(a, b, c)

# 값 교환
a, b = b, a 
print(a, b)

# 변수 타입
a=12345676543214321413413412341234124124123499999
print(a)
a=12.123123123123123123999999
print(a)
print(type(a))
a='student'
a="student"
print(a)
print(type(a))

# 출력방식
print("number")
a, b, c=1, 2, 3
print("number :", a, b, c)  
print(a, b, c, sep=', ')

# 자동 줄바꿈 해제
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')