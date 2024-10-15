def solution(a, b, n):
    cnt = 0
    while n >= a:
        c = (n // a) * b  
        cnt += c  
        n = (n % a) + c 

    return cnt