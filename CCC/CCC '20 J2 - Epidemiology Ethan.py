P = int(input())
N = int(input())
R = int(input())

infected_p = N
infected_l = N
time = 0

while infected_p <= P:
    time += 1
    infected_p += infected_l*R
    infected_l *= R
print(time)