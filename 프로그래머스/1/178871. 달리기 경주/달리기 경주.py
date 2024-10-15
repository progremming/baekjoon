# def solution(players, callings):
#     for calling in callings:
#         if calling in players: 
#             index = players.index(calling)
#             if index > 0: 
#                 players[index], players[index-1] = players[index-1], players[index] 
#     return players

def solution(players, callings):
    player_index = {player: index for index, player in enumerate(players)}
    
    for calling in callings:
        if calling in player_index:
            index = player_index[calling]
            if index > 0:
                players[index], players[index-1] = players[index-1], players[index]
                player_index[calling] = index - 1
                player_index[players[index]] = index
    
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

result = solution(players, callings)

print(result)
