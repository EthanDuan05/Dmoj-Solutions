N = int(input())
action = list(input())
opp_amo = 0
mine_amo = 0

mine_score = 0

for i in range(N):
    if action[i] == 'R':
        opp_amo += 1
        if mine_amo > 0:
            mine_score += 1
            mine_amo -= 1
        else:
            mine_amo += 1

    elif action[i] == 'B':
        mine_amo += 1

    elif action[i] == 'F':
        if opp_amo > 0:
            opp_amo -= 1
        else:
            if mine_amo > 0:
                mine_score += 1
                mine_amo -= 1
            else:
                mine_amo += 1

print(mine_score)
