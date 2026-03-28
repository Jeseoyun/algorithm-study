def solution(progresses, speeds):
    answer = []
    deploy = []
    for i in range(len(progresses)):
        rest_day = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] != 0:
            rest_day += 1
        deploy.append(rest_day)
    
    # print(deploy)
    
    current = deploy[0]
    count = 1
    
    for i in range(1, len(deploy)):
        if deploy[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = deploy[i]
            count = 1
    
    answer.append(count)  # 마지막 묶음
    
    return answer