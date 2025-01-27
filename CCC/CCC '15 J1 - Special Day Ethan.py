n = int(input())
c = int(input())
if n < 2:
    print('Before')
if n == 2 and c < 18:
    print('Before')
if n == 2 and c > 18:
    print('After')
if n > 2:
    print('After')
if n == 2 and c == 18:
    print('Special')