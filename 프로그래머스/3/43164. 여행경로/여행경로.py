## 오류 코드 - 테스트 케이스 1, 2번 오답
# def travel_path(tickets, ticket_idx, path, used):
#     if len(path) == len(tickets)+1:
#         return path
    
#     for next_idx, next_ticket in enumerate(tickets):
#         if next_ticket[0] == tickets[ticket_idx][1] and not used[next_idx]:
#             used[next_idx] = True
#             path.append(next_ticket[1])
#             result = travel_path(tickets, next_idx, path, used)
#             if result:
#                 return result
#             used[next_idx] = False


# def solution(tickets):
#     whole_path = []
#     used = [False] * len(tickets)
#     tickets = sorted(tickets, key=lambda x: x[1])
#     for idx, ticket in enumerate(tickets):
#         if ticket[0] == "ICN":
#             used[idx] = True
#             path = travel_path(tickets, idx, ticket, used)
#             whole_path.append(path)
            
#     for res in whole_path:
#         if res!=None:
#             return res


def travel_path(tickets, path, used):
    if len(path) == len(tickets) + 1:
        return path

    last_city = path[-1]

    for next_idx, (start, end) in enumerate(tickets):
        if start == last_city and not used[next_idx]:
            used[next_idx] = True
            result = travel_path(tickets, path + [end], used)
            if result:
                return result
            used[next_idx] = False


def solution(tickets):
    tickets.sort()  # 티켓을 알파벳 순으로 정렬
    for idx, (start, end) in enumerate(tickets):
        if start == "ICN":
            used = [False] * len(tickets)
            used[idx] = True
            path = travel_path(tickets, ["ICN", end], used)
            if path:
                return path
