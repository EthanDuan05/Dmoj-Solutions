N = int(input())
side = input().split(' ')
height = input().split(' ')
Side = []
Height = []
for i in range(N+1):
    Side.append(int(side[i]))
for i in range(N):
    Height.append(int(height[i]))
area = 0
for i in range(N):
    area += (Side[i] + Side[i+1]) * Height[i] / 2
print(area)

