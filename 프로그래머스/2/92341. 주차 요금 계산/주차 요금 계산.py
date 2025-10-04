from collections import defaultdict
import math


def calculate_fee(fees, total_minutes):
    # 기본 시간, 기본 요금, 단위 시간(분), 단위 요금
    base_time, base_fee, over_fee_min, over_fee = fees
    
    if total_minutes <= base_time:
        return base_fee
    
    additional = total_minutes - base_time
    
    return base_fee + math.ceil(additional / over_fee_min) * over_fee


def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m


def solution(fees, records):
    record_stack = dict()
    total_minutes = defaultdict(int)
    
    for record in records:
        record_time, car_num, in_out_info = record.split()
        
        if in_out_info == "IN":
            record_stack[car_num] = record_time
        else:  # OUT
            in_time = record_stack.pop(car_num)
            out_time = record_time
            duration = to_min(out_time) - to_min(in_time)
            
            total_minutes[car_num] += duration
            
    for rest_car, in_time in record_stack.items():
        out_time = "23:59"
        duration = to_min(out_time) - to_min(in_time)
        
        total_minutes[rest_car] += duration
        
    answer = []
    for car_num in sorted(total_minutes.keys()):
        fee = calculate_fee(fees, total_minutes[car_num])
        answer.append(fee)
        
    return answer