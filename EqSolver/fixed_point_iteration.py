# -*- coding: utf-8 -*-
# @Time    : 2022/12/3 15:42
# @Author  : Paul_Bao
# @FileName: fixed_point_iteration.py
# @Software: PyCharm

import sympy as sp

x = sp.symbols('x')
obj = x ** 3 - x ** 2 - 1
iter_func = 1 + 1 / x ** 2

while True:

