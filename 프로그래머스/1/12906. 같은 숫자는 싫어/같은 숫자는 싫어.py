def solution(arr):
    d=[]
    index = 0
    for i in arr:
        if len(d) == 0:
            d.append(arr[index])
        elif arr[index] == d[-1]:
            pass
        else:
            d.append(arr[index])
        index += 1
    return d