def solution(a, d, included):
    sums = 0
    for i in range(len(included)):
        if included[i] == bool(1):
            sums = sums + (a + (d*i))

    return sums


