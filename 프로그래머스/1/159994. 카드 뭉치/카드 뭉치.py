def solution(cards1, cards2, goal):
    car1 = 0
    car2 = 0

    a = "Yes"
    for i in goal:
        if car1 < len(cards1) and cards1[car1] == i:
            car1 += 1
        elif car2 < len(cards2) and cards2[car2] == i:
            car2 += 1
        else:
            a = "No"
            break

    return a