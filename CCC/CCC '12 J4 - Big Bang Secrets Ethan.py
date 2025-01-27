alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

alphabet_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16,
                'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                'Y': 25, 'Z': 26}


K = int(input())
line = list(input())

ans = []
for i in range(len(line)):
    letter = line[i]
    p = alphabet_dic[letter]
    shift_value = 3*(i+1)+K
    if p - shift_value < 0:
        final_shift = 26 - abs(p - shift_value)
    else:
        final_shift = p - shift_value

    ans.append(alphabet[final_shift-1])

print(''.join(ans))
