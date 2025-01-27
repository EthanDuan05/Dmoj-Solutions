N = int(input())

computer_1_name = ''
computer_1_score = -1

computer_2_name = ''
computer_2_score = -1

for i in range(N):
    Name, R, S, D = input().split()
    R = int(R)
    S = int(S)
    D = int(D)
    score = 2 * R + 3 * S + D

    if i == 0:
        computer_1_name = Name
        computer_1_score = score
        continue

    if (score > computer_1_score) or (score == computer_1_score and Name < computer_1_name):
        computer_2_name = computer_1_name
        computer_2_score = computer_1_score

        computer_1_name = Name
        computer_1_score = score

    elif score >= computer_2_score:
        if score > computer_2_score:
            computer_2_name = Name
            computer_2_score = score

        elif score == computer_2_score:
            if Name < computer_2_name:
                computer_2_name = Name
                computer_2_score = score

if computer_1_score != -1:
    print(computer_1_name)

if computer_2_score != -1:
    print(computer_2_name)
