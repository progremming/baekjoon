def solution(a, b):
    c = []
    d = []
    t = 1
    for i in range(len(b)):
        c = (a[b[i][0]-1:b[i][1]])  
        c.sort()
        for x in c:
            if t == b[i][2]:
                d.append(x)
            t = t+1
        t = 1
    return d