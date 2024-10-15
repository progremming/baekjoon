def solution(price, money, count):
    
    new_price = 0
    for i in range(1,count+1):
        new_price = new_price + (price * i)


    if new_price > money:
        return new_price - money
    else:
        return 0

