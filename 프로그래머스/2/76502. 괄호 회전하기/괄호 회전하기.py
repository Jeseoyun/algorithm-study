from collections import deque


def solution(s):
    combi = {"{": "}", "[": "]", "(": ")"}
    answer = 0
    
    for i in range(len(s)):
        new_s = deque(s)
        stack = []
        
        failed = False
        for target in new_s:
            # print("stack:", "".join(stack), "target:", target)
            
            if target in combi.keys():  # 여는거
                stack.append(target)
            
            else:  # 닫는거
                if not stack:
                    failed = True
                else:
                    if target == combi[stack[-1]]:  # 짝이 맞으면
                        stack.pop()
                    else:
                        failed = True

                    if failed:
                        break
            
        if not stack and not failed:
            answer += 1
        
        new_s.rotate()
        # print(new_s)
        s = "".join(new_s)
        
    return answer