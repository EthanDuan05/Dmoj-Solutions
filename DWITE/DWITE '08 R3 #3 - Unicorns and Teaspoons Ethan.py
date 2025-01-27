D_1 = {'oz in gill': 5,
       'oz in pt': 20,
       'oz in qt': 40,
       'oz in gal': 160,
       'oz in oz': 1,
       'gill in pt': 4,
       'gill in qt': 8,
       'gill in gal': 32,
       'gill in gill': 1,
       'pt in qt': 2,
       'pt in gal': 8,
       'pt in pt': 1,
       'qt in gal': 4,
       'qt in qt': 1}

D_2 = {'gill in oz': 5,
       'pt in oz': 20,
       'qt in oz': 40,
       'gal in oz': 160,
       'oz in oz': 1,
       'pt in gill': 4,
       'qt in gill': 8,
       'gal in gill': 32,
       'gill in gill': 1,
       'qt in pt': 2,
       'pt in pt': 1,
       'gal in pt': 8,
       'gal in qt': 4,
       'qt in qt': 1}

for _ in range(5):
    a, b, c, d = input().split()
    b = b + ' ' + c + ' ' + d
    a = int(a)

    if b in D_1:
       print(a // D_1[b])
    elif b in D_2:
        print(a * D_2[b])
