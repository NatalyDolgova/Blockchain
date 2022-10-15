import math
import random

def power_mod(x:int, pow:int, mod:int):
    assert type(x) is int
    assert type(pow) is int and pow >= 0
    assert type(mod) is int
    res = 1
    pow_res = 0
    while pow_res < pow:
        pow_res_1 = 2
        res1 = x
        while pow_res + pow_res_1 <= pow:
            res1 = (res1 * res1) % mod
            pow_res_1 *= 2
        pow_res_1 //= 2
        res = (res * res1) % mod
        pow_res += pow_res_1
    return res % mod

def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


# Ввод значення mod
m = int(input('введите делитель m = '))
# розв’язувати рівняння виду  a mod m = x
a = int(input('введите число a = '))
x = a % m
print ('Задача 2. Значение х = ', x)

# розв’язувати рівняння виду a^b mod m = x
a = int(input('введите число a = '))
b = int(input('введите степень числа a, b = '))
x = power_mod(a,b,m)
print ('Задача 3. Значение х = ', x)

# розв’язувати рівняння виду a*x ≡ b mod m
a = int(input('введите число a = '))
b = int(input('введите  число b = '))
d = linear_congruence(a, b, m)
print ('Задача 4. Значение х = ', d)

# * генерувати просте число у діапазоні від A до B

a = int(input('введите число a = '))
b = int(input('введите  число b = '))

z = random.randint(a, b)

while not IsPrime(z):
    z = random.randint(a, b)

print(z)