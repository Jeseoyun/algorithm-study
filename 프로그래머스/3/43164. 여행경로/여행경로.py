
def travel_path(tickets, ticket_idx, path, used):
    for next_idx, next_ticket in enumerate(tickets):
        if next_ticket[0] == tickets[ticket_idx][1] and not used[next_idx]:
            used[next_idx] = True
            path.append(next_ticket[1])
            travel_path(tickets, next_idx, path, used)
            
    if len(path) == len(tickets)+1:
        return path

def solution(tickets):
    whole_path = []
    used = [False] * len(tickets)
    tickets = sorted(tickets, key=lambda x: x[1])
    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            used[idx] = True
            path = travel_path(tickets, idx, ticket, used)
            whole_path.append(path)
            
    for res in whole_path:
        if res!=None:
            return res