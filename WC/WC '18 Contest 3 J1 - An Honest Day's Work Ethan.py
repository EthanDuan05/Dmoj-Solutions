p = int(input())
b = int(input())
d = int(input())
num = p // b  # number of cap
price_1 = num * d  # revenue for only cap
price_2 = p - num * b  # remainder
price_t = 0
if price_2 >= 0:
    price_t = price_1 + price_2
elif price_2 < 0:
    price_t = price_1
print(int(price_t))