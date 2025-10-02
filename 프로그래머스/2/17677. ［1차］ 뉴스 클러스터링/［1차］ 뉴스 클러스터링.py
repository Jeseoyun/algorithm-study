# 자카드 유사도: 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
# 

from collections import Counter


class multiSet:
    def __init__(self, str):
        self.element = []
        
        s = str.lower()
        
        for i in range(len(str)-1):
            a, b = s[i], s[i+1]
            
            if a.isalpha() and b.isalpha():
                self.element.append(a+b)
        
        # print(self.element)
    
    
    def union(self, target):
        c1 = Counter(self.element)
        c2 = Counter(target.element)
        
        return list((c1|c2).elements())
        

    def intersection(self, target):
        c1 = Counter(self.element)
        c2 = Counter(target.element)
        
        return list((c1&c2).elements())



def solution(str1, str2):
    s1_ms = multiSet(str1)
    s2_ms = multiSet(str2)
    
    if s1_ms.element == s2_ms.element:
        return 65536
    
    inter = s1_ms.intersection(s2_ms)
    uni = s1_ms.union(s2_ms)
    
    return int(len(inter)/len(uni)*65536)
