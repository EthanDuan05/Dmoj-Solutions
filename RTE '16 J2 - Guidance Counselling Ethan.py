from queue import PriorityQueue

dic_1 = {'blue': 1, 'pink': 2, 'green': 3}
dic_2 = {1: 'blue', 2: 'pink', 3: 'green'}
Q = PriorityQueue()

T = int(input())

for _ in range(T):
    line = input().split()
    if len(line) > 1:
        category = line[1].lower()
        number = line[2]
        Q.put((dic_1[category], int(number)))
    else:
        ans = Q.get()
        print(dic_2[ans[0]].upper(), ans[1])
