#***********************Vice-Versa of above program***********
def binary():
    n = input('Enter binary number: ')
    a = 0
    r = 0
    t = int(n)
    while n!=0:
        q = int(n)%10
        n = int(n)//10
        a += 1
    print(f'number of digits in {t}: ', a)
    a = a
    a1 = 0
    while a1 < a:
        q = t%10
        r = r + q*pow(2,a1)
        t = t//10
        a1 += 1
    print(r)

def octal():
    n = input('Enter octal number: ')
    a = 0
    r = 0
    t = int(n)
    while n!=0:
        q = int(n)%10
        n = int(n)//10
        a += 1
    print(f'number of digits in {t}: ', a)
    a = a
    a1 = 0
    while a1 < a:
        q = t%10
        r = r + q*pow(8,a1)
        t = t//10
        a1 += 1
    print(r)

def hexadecimal():
    n = input('Enter hexadeecimal number: ')
    a = 0
    r = 0
    t = int(n)
    while n!=0:
        q = int(n)%10
        n = int(n)//10
        a += 1
    print(f'number of digits in {t}: ', a)
    a = a
    a1 = 0
    while a1 < a:
        q = t%10
        r = r + q*pow(16,a1)
        t = t//10
        a1 += 1
    print(r)



choice = int(input('Enter choice\n1. Binary to dec\n2. Octal to dec\n3. hexadecimal to dec '))
if choice == 1:
    binary()
if choice == 2:
    octal()
if choice == 3:
    hexadecimal()