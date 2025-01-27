line = input()
count = [0]*len(line)
string = input()

for i in range(len(line)):
    if line[i] in string:
        count[i] += 1

for k in range(len(count)):
    a = k+len(string)
    if count[k:k+1] == 1:
        print(k)
