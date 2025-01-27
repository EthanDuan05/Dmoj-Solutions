N = int(input())
Letter = {1: 'A', 2: 'B', 3: 'C', 4: 'D',
          5: 'E', 6: 'F', 7: 'G', 8: 'H',
          9: 'I', 10: 'J', 11: 'K', 12: 'L',
          13: 'M', 14: 'N', 15: 'O', 16: 'P',
          17: 'Q', 18: 'R', 19: 'S', 20: 'T',
          21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
L = []
for _ in range(N):
    num = int(input())
    L.append(num)

flag = True
ind  = -1
sentence = ''
while flag:
    ind += 1
    num = L[ind]
    if num == 0:
        flag = False
    else:
        ind += num
        if L[ind] == 0:
            flag = False
        else:
            sentence += Letter[L[ind]]

print(sentence)