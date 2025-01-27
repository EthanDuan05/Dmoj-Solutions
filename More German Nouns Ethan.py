import string
N = int(input())
in_punc = set(string.punctuation)

for i in range(N):
    line = input().split(' ')
    for s in line:
        if s[0].isupper():
            if s[-1] in in_punc:
                print(s[0:-1])
            else:
                print(s)