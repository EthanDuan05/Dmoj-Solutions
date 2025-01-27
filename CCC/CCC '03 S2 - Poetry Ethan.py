Vowel = ['a', 'e', 'i', 'o', 'u']
n = int(input())

ans = []
for i in range(n):
    line_1 = input().lower().split()
    line_2 = input().lower().split()
    line_3 = input().lower().split()
    line_4 = input().lower().split()
    Letter = [line_1[len(line_1) - 1], line_2[len(line_2) - 1],
              line_3[len(line_3) - 1], line_4[len(line_4) - 1]]

    Type = []
    for k in Letter:
        if 'a' or 'e' or 'i' or 'o' or 'u' in k:
            Type.append(True)
        else:
            Type.append(False)

    Rhyme = []
    for s in range(4):
        if Type[s] == True:
            word = Letter[s]
            position = -1
            for m in range(len(word)):
                if word[m] in Vowel:
                    position = m
            if position == -1:
                Rhyme.append(word)
            else:
                Rhyme.append(word[position:])
        elif Type[s] == False:
            Rhyme.append(Letter[s])

    if Rhyme[0] == Rhyme[1] == Rhyme[2] == Rhyme[3]:
        ans.append('perfect')
    elif Rhyme[0] == Rhyme[1] and Rhyme[2] == Rhyme[3]:
        ans.append('even')
    elif Rhyme[0] == Rhyme[2] and Rhyme[1] == Rhyme[3]:
        ans.append('cross')
    elif Rhyme[0] == Rhyme[3] and Rhyme[1] == Rhyme[2]:
        ans.append('shell')
    else:
        ans.append('free')

for i in ans:
    print(i)