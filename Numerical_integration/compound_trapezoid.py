# -*- coding: utf-8 -*-
# @Time    : 2022/11/17 21:18
# @Author  : Paul_Bao
# @FileName: compound_trapezoid.py
# @Software: PyCharm
# @mail    ：oye20000101@gmail.com


def eqn(x):
    return x / (4 + x ** 2)


def Hn(a, b, n):
    h = (b - a) / n
    z = 0
    for i in range(1, n + 1):
        z += h * eqn(a + (2 * i - 1) * h / 2)
    return z


a = 0
b = 1
n = 1
h = b - a
T = 0.5 * h * (eqn(a) + eqn(b))  # n = 1
while True:
    n *= 2
    h /= 2
    if abs((T + Hn(a, b, n)) / 2 - T) > 1e-6:
        T = (T + Hn(a, b, n)) / 2
        if n == 8:
            print((T + Hn(a, b, n))/2)
    else:
        break
print((T + Hn(a, b, n)) / 2)
print(n)
