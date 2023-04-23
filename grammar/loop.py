'''
반복문(for, while)
'''

# a=range(1, 11)
# print(list(a))

for i in range(10, 0, -2):
    print(i)
    
i=1
while(i<10):
    print(i)
    i=i+1
    
while True:
    print(i)
    if i==0:
        break
    i-=1
    
    

for i in range(1,11):
    if i%2==0:
        continue
    print(i)
    
    
# for문이 break에 걸리지 않고 종료되면 else문 실행
for i in range(1,11):
    print(i)
    if i>15:
        break
else:
    print(20) 
    
    

