def solution(players, callings):
    players_dict = {}
    for i, player in enumerate(players):
        players_dict[player] = i
    for calling in callings:
        rank = players_dict[calling]
        players_dict[calling] -= 1
        players_dict[players[rank - 1]] += 1
        
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
    return players