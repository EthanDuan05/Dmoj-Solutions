import queue
from queue import PriorityQueue

N = int(input())
D = {'Deluxe Tuna Bitz': 0,
     'Bonito Bitz': 1,
     'Sashimi': 2,
     'Ritzy Bitz': 3}

D_1 = {}

for _ in range(N):
    food = input()
    if food not in D_1:
        D_1[food] = 1
    else:
        D_1[food] += 1

print(D_1)

queue = queue.PriorityQueue()

for i in D_1:
    queue.put((D_1[i], int(D[i]), i))

ANS = []
while not queue.empty():

    ANS.append([queue.get()[0], queue.get()[2]])

print(ANS)