T = int(input())
specific_value = [1.5, 4.5]

ans = []
for _ in range(T):
    world, level = map(int, input().split('-'))
    value = world + 0.25*level
    if value > 4.5:
        need = (9 - value) // 0.25 + 1
        ans.append(need)
    else:
        if value in specific_value:
            if value == 1.5:
                need = 7
                ans.append(need)
            elif value == 4.5:
                need = 5
                ans.append(need)
        else:
            if value < 1.5:
                stage_1 = (1.5 - value) // 0.25 + 1
                stage_2 = 6
                need = stage_1 + stage_2
                ans.append(need)
            elif 1.5 < value < 4.5:
                stage_1 = abs(4.5 - value) // 0.25 + 1
                stage_2 = 4
                need = stage_1 + stage_2
                ans.append(need)

for i in ans:
    print('%.0f'%i)





