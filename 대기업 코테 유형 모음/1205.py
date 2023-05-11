N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))
    if N == P and scores[N-1] >= new_score:
        print(-1)
    else:
        for i in range(N):
            if new_score >= scores[i]:
                print(i+1)
                new_score=-1
                break
        if new_score != -1:
            print(N+1)