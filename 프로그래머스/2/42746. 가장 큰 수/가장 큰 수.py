def solution(numbers):
    if numbers.count(0) == len(numbers):
        return "0"
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    
    return "".join(numbers)