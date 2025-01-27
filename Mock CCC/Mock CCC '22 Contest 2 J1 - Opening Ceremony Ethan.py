a, b, c = map(int, input().split())
Ta, Tb, Tc = map(int, input().split())
num = Ta+Tb+Tc
ticket = a*Ta+b*Tb+c*Tc

print(num, ticket)