time, minutes = map(int, input().split())
add = int(input())

add_hour = 0
minutes += add
while minutes >= 60:
    minutes -= 60
    add_hour += 1

time += add_hour
while time >= 24:
    time -= 24

print(time, minutes)