string = input()
words = [string, string[::-1]]
row = int(input())
column = int(input())

graph = []

for _ in range(row):
    line = input().strip()
    graph.append(line)

cnt = 0
for i in range(row):
    for s in range(column):
        for w in words:
            # horizontal
            state_h = True
            for k in range(len(w)):
                if s + k > column - 1:
                    state_h = False
                    break

                if graph[i][s + k] != w[k]:
                    state_h = False
                    break

            if state_h:
                cnt += 1
            '''
            # vertical
            state_v = True
            for k in range(len(w)):
                if i + k > row - 1:
                    state_v = False
                    break

                elif graph[i + k][s] != w[k]:
                    state_v = False
                    break

                if k == 0 or k == len(w)-1:
                    continue

                # vertical L shape downward
                state_v_l_down = True
                for r in range(1, len(w) - k):
                    if s + r > column - 1:
                        state_v_l_down = False
                        break

                    if graph[i + k][s + r] != w[k + r]:
                        state_v_l_down = False
                        break

                if state_v_l_down:
                    cnt += 1
                    # print(i, s, graph[i][s])

                state_v_l_down = True
                for r in range(1, len(w) - k):
                    if s - r < 0:
                        state_v_l_down = False
                        break

                    if graph[i + k][s - r] != w[k + r]:
                        state_v_l_down = False
                        break

                if state_v_l_down:
                    cnt += 1

            if state_v:
                cnt += 1

            # vertical L shape upward
            state_v_l_up = True
            for k in range(len(w)):
                if i - k < 0:
                    state_v_l_up = False
                    break

                for r in range(1, len(w) - k):
                    if s + r > column - 1:
                        state_v_l_up = False
                        break

                    if graph[i - k][s + r] != w[k + r]:
                        state_v_l_up = False
                        break

                    if s - r < 0:
                        state_v_l_up = False
                        break

                    if graph[i - k][s - r] != w[k + r]:
                        state_v_l_up = False
                        break

            if state_v_l_up:
                cnt += 1
            '''

            # diagonal_down
            state_d_down = True
            for k in range(len(w)):
                if i + k > row - 1 or s + k > column - 1:
                    state_d_down = False
                    break
                elif graph[i + k][s + k] != w[k]:
                    state_d_down = False
                    break

            if state_d_down:
                cnt += 1

            # diagonal_up
            state_d_up = True
            for k in range(len(w)):
                if i - k < 0 or s + k > column-1:
                    state_d_up = False
                    break
                elif graph[i - k][s + k] != w[k]:
                    state_d_up = False
                    break

            if state_d_up:
                cnt += 1


print(cnt)
