N = int(input())
In_hand = []
Cards = {2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:16, 11:4}

for _ in range(N):
    card = int(input())
    In_hand.append(card)
    Cards[card] -= 1

X = 21 - sum(In_hand)

Larger = 0
Smaller = 0

for i in Cards:
    if i > X:
        Larger += Cards[i]

    if i <= X:
        Smaller += Cards[i]

if Larger >= Smaller:
    print('DOSTA')
else:
    print('VUCI')