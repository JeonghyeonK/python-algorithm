import sys
input = sys.stdin.readline

N = int(input())
ball_list = input().strip()

left = [0, 0]
right = [0, 0]
red, blue = 0, 0

for ball in ball_list:
    if ball == 'R':
        red += 1
    else:
        blue += 1

left[0] = ball_list[0]
for ball in ball_list:
    if ball == left[0]:
        left[1] += 1
    else:
        break
right[0] = ball_list[-1]
for i in range(len(ball_list)-1, -1, -1):
    if ball_list[i] == right[0]:
        right[1] += 1
    else:
        break

#print(red, blue)
#print(left, right)
answer = 0

if left[0] == right[0]:
    if left[1] > right[1]:
        if left[0] == 'R':
            answer = min(red - left[1], blue)
        else:
            answer = min(blue - left[1], red)
    else:
        if right[0] == 'R':
            answer = min(red - right[1], blue)
        else:
            answer = min(blue - right[1], red)
else:
        if left[0] == 'R':
            answer = min(red - left[1], blue - right[1])
        else:
            answer = min(blue - left[1], red - right[1])
    
        
print(answer)


'''
양쪽 색깔이 같으면
양쪽 중 같은 색이 더 많이 붙은 쪽으로 몰기
or 다른 색인 쪽이 모두 한쪽으로 이동하기

양쪽 색깔이 다르면
양쪽 색깔로 각자 붙어서 세기'''