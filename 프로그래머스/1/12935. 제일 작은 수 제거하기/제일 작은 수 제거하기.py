def solution(arr):
    mins = min(arr)
    if len(arr) == 1:
        return [-1]
    arr.remove(mins)
    return arr