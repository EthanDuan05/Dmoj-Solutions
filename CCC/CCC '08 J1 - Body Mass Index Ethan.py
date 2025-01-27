W = float(input())
H = float(input())
K = H*H
B = W/K
if B > 25:
    print('Overweight')
if 18.5 <= B <= 25:
    print('Normal weight')
if B < 18.5:
    print('Underweight')