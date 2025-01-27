p_c = 0
p_n = 0

num_fish = int(input())
for i in range(num_fish):
    w, l = input().split()
    w = int(w)
    l = int(l)
    product_c = w * l
    if product_c > p_c:
        p_c = product_c
    else:
        p_c = p_c
    if num_fish != num_fish:
        break

num_fish = int(input())
for m in range(num_fish):
    w, l = input().split()
    w = int(w)
    l = int(l)
    product_n = w * l
    if product_n > p_n:
        p_n = product_n
    else:
        p_n = p_n

if p_c > p_n:
    print('Casper')
elif p_n > p_c:
    print('Natalie')
else:
    print('Tie')