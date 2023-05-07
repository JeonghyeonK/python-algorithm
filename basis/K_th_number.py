T=int(input())


for i in range(T):
    N, s, e, k=map(int, input().split())
    
    arr=list(map(int,input().split()))
    
    arr=arr[s-1:e]
    
    arr.sort()    
    # print("#", i+1, ' ', arr[k-1], sep='')은 아래와 같음
    print("#%d %d" %(i, arr[k-1]))
    