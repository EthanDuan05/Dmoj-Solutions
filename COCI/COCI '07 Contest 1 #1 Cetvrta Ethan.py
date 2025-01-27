x_element = {}
y_element = {}

for _ in range(3):
    x, y = map(int, input().split())

    if x not in x_element:
        x_element[x] = 1
    else:
        x_element[x] += 1

    if y not in y_element:
        y_element[y] = 1
    else:
        y_element[y] += 1

a = min(x_element.values())
b = min(y_element.values())

new_coordinate = []
for i in x_element:
    if x_element[i] == a:
        new_coordinate.append(i)
        break

for i in y_element:
    if y_element[i] == b:
        new_coordinate.append(i)
        break

print(' '.join(map(str, new_coordinate)))