def solution(k, score):
    d = []  
    sc = []  

    for i in range(len(score)):
        if i < k:
            d.append(score[i])  
            d.sort()
            sc.append(d[0]) 
        else:
            if score[i] > d[0]: 
                d[0] = score[i] 
                d.sort() 
            
            sc.append(d[0]) 

    return sc
