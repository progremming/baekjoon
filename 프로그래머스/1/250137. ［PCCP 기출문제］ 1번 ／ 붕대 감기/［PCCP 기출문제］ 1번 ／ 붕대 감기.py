def solution(bandage, health, attacks):
    ch = health
    time = 0
    bonus = 0

    for i in range(len(attacks)):
        if ch <= 0:
            break
        
        while True:
            print(time, bonus, ch)
            time = time + 1
            bonus = bonus + 1
            
            if attacks[i][0] == time:
                ch = ch - attacks[i][1]
                bonus = 0
                break
            else:
                if ch != health:
                    if bonus == bandage[0]:
                        ch = ch + bandage[1] + bandage[2]
                        bonus = 0
                        if ch > health:
                            ch = health
                    else:
                        ch = ch + bandage[1]
                        if ch > health:
                            ch = health
    if ch <= 0:
        ch = -1
    
    return ch
 

