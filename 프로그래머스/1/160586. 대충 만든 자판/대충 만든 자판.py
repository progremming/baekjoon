def solution(keymap, targets):
    sums = 0

    sumslist = []

    index = 1


    d = []
    for z in range(0,len(targets)):
        for c in targets[z]:
            for i in range(0,len(keymap)):
                for x in keymap[i]:
                    if x == c:
                        d.append(index)
                    index +=1
                index = 1
            if len(d) == 0:
                sums = -1
                break
            else:
                sums = sums + min(d)
            d = []
        sumslist.append(sums)
        sums = 0
    return sumslist