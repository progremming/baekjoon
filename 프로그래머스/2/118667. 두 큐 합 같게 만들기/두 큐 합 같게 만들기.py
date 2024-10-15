from collections import deque

def solution(queue1, queue2):

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    

    sum1, sum2 = sum(queue1), sum(queue2)
    total_sum = sum1 + sum2
    

    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2  
    cnt = 0  
    max_operations = len(queue1) + len(queue2) * 2  


    while cnt <= max_operations:
        if sum1 == target:
            return cnt  
        
        if sum1 > target:
            
            val = queue1.popleft()
            sum1 -= val
            queue2.append(val)
        else:
            
            val = queue2.popleft()
            sum2 -= val
            queue1.append(val)
            sum1 += val
        
        cnt += 1
    
    return -1  
