def solution(a,b):
    i,j = 0,0
    ins = []

    set1 = list(a)
    set2 = list(b)
    set1.sort()
    set2.sort()

    while i < len(set1) and j < len(set2):
        if set1[i] == set2[j]:
            ins.append(set1[i])
            i = i + 1
            j = j + 1
        elif set1[i] > set2[j]:
            j = j + 1
        else:
            i = i + 1


    if len(ins) == 0:
        return "-1"
    if ins[-1] == "0":
        return "0"
    ins.sort()
    ins.reverse()
    c = ''.join(ins)
    return str(c)