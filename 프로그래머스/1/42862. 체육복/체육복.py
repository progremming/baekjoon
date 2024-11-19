
def solution(n,lost,reserve):

    
    nens = n - len(lost)

    for i in lost[:]: 
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            nens += 1   
    lost.sort()
    for i in lost[:]:
        if i-1 in reserve:
            lost.remove(i)
            reserve .remove(i-1)
            nens += 1
        elif  i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
            nens += 1

    return nens
