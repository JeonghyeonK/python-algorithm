tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def solution(tickets):
    answer = []
    
    
    tickets.sort()
    lst = []
    for airport in tickets:
        for i in range(2):
            if airport[i] in lst:
                lst.remove(airport[i])
            else:
                lst.append(airport[i])
    
    print(lst)
    lst.sort()
    start = lst[0]
    print(start)
    return answer

solution(tickets)
print(tickets)