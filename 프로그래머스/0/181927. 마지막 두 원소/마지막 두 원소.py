def solution(lists):
    if lists[-1] > lists[-2]:
        lists.append(lists[-1] - lists[-2])
        return lists
    else:
        lists.append(lists[-1]*2 )
        return lists