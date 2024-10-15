import math

def solution(s):
    if len(s) % 2 == 1:
        avg = math.floor(len(s) / 2)  
        return s[avg]
    else:
        avg = math.floor(len(s) / 2)  
        return s[avg - 1: avg + 1]
