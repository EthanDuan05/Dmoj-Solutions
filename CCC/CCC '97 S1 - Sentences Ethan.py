n = int(input())

for _ in range(n):
    s = int(input())
    v = int(input())
    o = int(input())

    subject = []
    verb = []
    objeccts = []

    for _ in range(s):
        ss = input()
        subject.append(ss)

    for _ in range(v):
        vv = input()
        verb.append(vv)

    for _ in range(o):
        oo = input()
        objeccts.append(oo)

    for i in subject:
        for b in verb:
            for c in objeccts:
                print(i+' '+b+' '+c+'.')
