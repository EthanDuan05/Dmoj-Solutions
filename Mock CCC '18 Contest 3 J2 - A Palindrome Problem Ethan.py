line = input()
Dbug = False
Flag = False

def is_palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False

for i in range(len(line)):
    a = line[0:i]
    b = line[i:len(line)]
    if is_palindrome(a) and is_palindrome(b):
        if len(a) > 0 and len(b) > 0:
            Flag = True

            if Dbug:
                print(i)
                print(a)
                print(b)
            break

if Flag:
    print('YES')
else:
    print('NO')

