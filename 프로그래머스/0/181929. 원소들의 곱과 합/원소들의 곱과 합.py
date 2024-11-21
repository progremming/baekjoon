def solution(lists):
    sums = sum(lists) * sum(lists)
    sums2 = 1
    for i in lists:
        sums2 = sums2 * i 
    if sums2 < sums:
        return 1
    else:
        return 0