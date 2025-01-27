N = int(input())

line = list(map(int, input().split()))

Original = line.pop(0)


def finding_gcf(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


for i in range(N-1):
    compare = line[i]
    if compare == Original:
        print('1/1')
    else:
        GCF = finding_gcf(Original, compare)
        print(str(Original//GCF)+'/'+str(compare//GCF))