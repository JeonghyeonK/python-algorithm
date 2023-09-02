T = int(input())

for _ in range(T):
    N = int(input())
    price_list = list(map(int, input().split()))
    
    high_point_list = list()
    before_high_point_idx = 0
    for _ in range(len(price_list)):
        low_point_num = 10001
        high_point_num = 0
        high_point_idx = 0
        for i in range(before_high_point_idx, len(price_list)):
            if price_list[i] <= low_point_num:
                low_point_num = price_list[i]
                
            elif price_list[i] >= high_point_num:
                high_point_num = price_list[i]
                high_point_idx = i
        if high_point_num <= low_point_num:
            break
        else:
            high_point_list.append(high_point_idx)
            before_high_point_idx = high_point_idx
    
    #print(high_point_list)
    
    
    
    
    answer = 0
    before_high_point_idx = -1
    for high_point_idx in high_point_list:
        buy_total = 0
        buy_cnt = 0
        for i in range(before_high_point_idx+1, high_point_idx):
            if price_list[i] < price_list[high_point_idx]:
                buy_total += price_list[i]
                buy_cnt += 1
        answer = answer + (price_list[high_point_idx] * buy_cnt - buy_total)
        before_high_point_idx = high_point_idx
        
        
    print(answer)
    
    


# 1 3 1 9 5 5 6 3 4 3 2 1 1
# b b b s b b s b s -
# 미래 가격 중 현재 가격보다 비싼 가격이 존재하면 무조건 buy
# 산 주식은 무조건 미래의 모든 주가 중 가장 비싼 날 팔아야 함
# 가장 비싼 날이 언젠지 탐색 -> 그 날 이후의 날들 중 가장 비씬날 탐색 -> 반복
# 가장 비싼 날 이후의 리스트에서 새로운 고점을 정할 때, 그 점 이전의 값 중 더 싼 값이 있어야 고점이 될 수 있음
# 그래서 고점 이후로는 하락이 멈출 때까지는 고점 지정 불가

# 27 - 5 + 2 + 1