N = int(input())
pattern = input().split('*')

for i in range(N):
    word = input()
    if word[:len(pattern[0])] == pattern[0] and word[len(word)-len(pattern[-1]):] == pattern[-1]:
        if word[len(pattern[0])+1: len(word)-len(pattern[-1])].islower() or word[len(pattern[0])+1: len(word)-len(pattern[-1])] == '':
            if len(pattern[0]) + len(pattern[-1]) > len(word):
                print('NE')
            else:
                print('DA')
    else:
        print('NE')