def is_nasty_number(n):
    factors = []

    # Find all factors of the number
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))

    # Check for nasty condition
    for i in range(len(factors)):
        for j in range(i + 1, len(factors)):
            if abs(factors[i][0] - factors[i][1]) == sum(factors[j]) or sum(factors[i]) == abs(
                    factors[j][0] - factors[j][1]):
                return True

    return False


N = int(input())
for _ in range(N):
    number = int(input())

    if is_nasty_number(number):
        print(f"{number} is nasty")
    else:
        print(f"{number} is not nasty")