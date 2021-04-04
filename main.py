#*************Convert decimal to binary, octal, hexadecimal*****************
rev = 0
a = 0
def binary(x):
    global rev, a, ans
    while x!=0:
        r = x%2
        x = x//2
        ans.append(str(r))
    for i in ans[::-1]:
        print(i, end=" ")
    print()
             
def octal(x):
    global rev, a
    while x!=0:
        r = x%8
        x = x//8
        ans.append(str(r))
    for i in ans[::-1]:
        print(i, end=" ")
    print()
    
def hexadecimal(x):
    global rev, a
    while x!=0:
        r = x%16
        x = x//16
        ans.append(str(r))
    for i in ans[::-1]:
        print(i, end=" ")
    print()
while True:
    ans = list()
    num = int(input('Enter decimal number and select operation: '))
    choice = int(input('1. Binary\n2. Octal\n3. Hexadecimal\n4. Exit '))

    if choice == 1:
        binary(num)
    if choice == 2:
        octal(num)
    if choice == 3:
        hexadecimal(num)
    if choice == 4:
        break


