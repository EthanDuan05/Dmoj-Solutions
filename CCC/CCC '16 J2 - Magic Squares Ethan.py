v_1 = 0
v_2 = 0
v_3 = 0
v_4 = 0

h_1 = 0
h_2 = 0
h_3 = 0
h_4 = 0

v = []
H = []


for i in range(4):
    line = input().split()
    v_1 += int(line[0])
    v_2 += int(line[1])
    v_3 += int(line[2])
    v_4 += int(line[3])

    for k in range(1):
        h_1 = int(line[0]) + int(line[1]) + int(line[2]) + int(line[3])
        h_2 = int(line[0]) + int(line[1]) + int(line[2]) + int(line[3])
        h_3 = int(line[0]) + int(line[1]) + int(line[2]) + int(line[3])
        h_4 = int(line[0]) + int(line[1]) + int(line[2]) + int(line[3])


v.append(v_1)
v.append(v_2)
v.append(v_3)
v.append(v_4)
H.append(h_1)
H.append(h_2)
H.append(h_3)
H.append(h_4)

cnt = 0
for s in v:
    for t in H:
        if int(s) == int(t):
            cnt = cnt
        else:
            cnt += 1
if cnt > 0:
    print('not magic')
elif cnt == 0:
    print('magic')