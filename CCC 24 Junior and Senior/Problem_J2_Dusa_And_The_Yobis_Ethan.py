Initial = int(input())

State = True
while State:
    NUM = int(input())
    if NUM >= Initial:
        State= False
    else:
        Initial += NUM

print(Initial)