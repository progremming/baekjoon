def solution(n):
    low = 0
    hig = n
    while  low <= hig:
        mid = (low + hig) // 2
        if mid * mid == n:
            return (mid +1) * (mid+1)
        elif mid * mid < n:
            low = mid + 1
        else:
            hig = mid - 1

    return -1