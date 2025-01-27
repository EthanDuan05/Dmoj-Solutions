P = int(input())
T = int(input())

present = {}
teacher = {}

for _ in range(P):
    name = input()
    price = float(input())
    present[price] = name

for _ in range(T):
    name_t = input()
    rate = int(input())
    teacher[rate] = name_t

p_s = []
t_s = []

for i in present.keys():
    p_s.append(i)

for i in teacher.keys():
    t_s.append(i)

p_s.sort()
t_s.sort()

ans = []
while t_s and p_s:
    a = t_s.pop(-1)
    b = p_s.pop(-1)
    ans.append(teacher[a] + ' ' + 'will get a' + ' ' + present[b])

while ans:
    lll = ans.pop(-1)
    print(lll)