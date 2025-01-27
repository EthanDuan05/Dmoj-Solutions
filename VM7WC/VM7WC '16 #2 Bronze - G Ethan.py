original_image = ['GGGGG',
                  'G....',
                  'G..GG',
                  'G...G',
                  'GGGGG']

N = int(input())

new_image = []
for i in original_image:
    new_i = i[0]*N + i[1]*N + i[2]*N + i[3]*N + i[4]*N
    for _ in range(N):
        new_image.append(new_i)

for i in new_image:
    print(i)