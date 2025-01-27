# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')
name='Ethan'
print(id(name))
print(type(name))
print(name)

s1=4
s2='44.4'
ff=True
print(type(s1),type(s2),type(ff))

print(type(s1),type(str(s1)),type(s2),type(str(s2)),type(ff),type(str(ff)))
print(type(s1),type(s2),type(ff))
print(str(s1),str(44.4),str(ff))
print(type(s1),type(s2),type(ff))

a=input('one number:')
a=int(a)
b=input('another number:')
b=int(b)
print(a+b)

p=input('name')
t=input('age')

print('My name is '+p)
print('I am '+ t,'years old now')
