T = int(input())

for _ in range(T):
    case_number = int(input())
    string = list(input())
    length = len(string)
    string_number = int(input())
    foot_notes = list(map(int, input().split()))
    ans = []

    current_ind = 0
    for i in range(string_number):
        if current_ind + foot_notes[i] >= length:
            while current_ind + foot_notes[i] >= length:
                difference = length - current_ind
                current_ind = foot_notes[i] - difference

        elif current_ind + foot_notes[i] <= -length:
            difference = length - abs(current_ind)
            current_ind = foot_notes[i] + difference

        elif current_ind + foot_notes[i] < length:
            current_ind += foot_notes[i]

        # print(current_ind, 'number')
        # print(string[current_ind], 'letter')

        ans.append(string[current_ind])

    print(case_number, ''.join(ans))