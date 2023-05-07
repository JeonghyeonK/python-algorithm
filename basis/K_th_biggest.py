N, K=map(int, input().split())
    
arr=list(map(int,input().split()))

arr.sort(reverse=True)

new_arr=[]
n=0
while(True):
    if new_arr[-1]!=arr[n]:
        new_arr.append(arr[n])
        if len(new_arr)==5:
            break
    n+=1

num1=new_arr[0]+new_arr[1]+new_arr[4]
num2=new_arr[0]+new_arr[2]+new_arr[3]
num3=new_arr[1]+new_arr[2]+new_arr[3]
print(max(num1, num2, num3))