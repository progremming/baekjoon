def solution(progresses, speeds):
    cnt_list = []
    
    
    while progresses:
       
        for x in range(len(progresses)):
            progresses[x] += speeds[x]  

        cnt = 0  

        
        while progresses and progresses[0] >= 100:
            cnt += 1 
            progresses.pop(0)  
            speeds.pop(0)  

        if cnt > 0:  
            cnt_list.append(cnt) 

    return cnt_list  