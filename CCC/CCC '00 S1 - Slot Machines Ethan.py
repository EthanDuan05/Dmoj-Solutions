jars = int(input())

machine1 = int(input())
machine2 = int(input())
machine3 = int(input())

cnt = 0

while jars > 0:
    jars -= 1
    cnt += 1
    machine1 += 1
    if machine1 == 35:
        jars += 30
        machine1 = 0
    if jars == 0:
        break

    jars -= 1
    cnt += 1
    machine2 += 1
    if machine2 == 100:
        jars += 60
        machine2 = 0
    if jars == 0:
        break

    jars -= 1
    cnt += 1
    machine3 += 1
    if machine3 == 10:
        jars += 9
        machine3 = 0
    if jars == 0:
        break

print('Martha plays', cnt, 'times before going broke.')