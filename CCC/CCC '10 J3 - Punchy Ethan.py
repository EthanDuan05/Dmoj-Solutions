import math

D = {}
while True:
    command = input().split()

    if command[0] == '1':
        D[command[1]] = int(command[2])
    elif command[0] == '2':
        if command[1] in D:
            print(D[command[1]])
        else:
            print(0)

    elif command[0] == '3':
        Sum = D[command[1]] + D[command[2]]
        D[command[1]] = Sum
    elif command[0] == '4':
        Prod = D[command[1]] * D[command[2]]
        D[command[1]] = Prod
    elif command[0] == '5':
        Diff = D[command[1]] - D[command[2]]
        D[command[1]] = Diff
    elif command[0] == '6':
        Quo = math.floor(D[command[1]] / D[command[2]])
        D[command[1]] = Quo
    elif command[0] == '7':
        break
