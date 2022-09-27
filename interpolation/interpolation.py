import numpy as np


def linearInter(x_in, xarr, yarr):
    for i in range(len(xarr)):
        if x_in > xarr[i]:
            result = yarr[i] + (yarr[i + 1] - yarr[i]) / (xarr[i + 1] - xarr[i]) * (x_in - xarr[i])
            break
        elif x_in > xarr[len(xarr)]:
            return "unable to interpolation!"
    return result


def quadraticInter(x_in, xarr, yarr):
    for i in range(len(xarr)):
        if x_in > xarr[i]:
            result = yarr[i] * (x_in - xarr[i + 1]) * (x_in - xarr[i + 2]) / (
                    (xarr[i] - xarr[i + 1]) * (xarr[i] - xarr[i + 2])) + \
                     yarr[i + 1] * (x_in - xarr[i]) * (x_in - xarr[i + 2]) / (
                             (xarr[i + 1] - xarr[i]) * (xarr[i + 1] - xarr[i + 2])) + \
                     yarr[i + 2] * (x_in - xarr[i]) * (x_in - xarr[i + 1]) / (
                             (xarr[i + 2] - xarr[i]) * (xarr[i + 2] - xarr[i + 1]))
            break
        elif x_in > xarr[len(xarr)]:
            return "unable to interpolation!"
    return result


def lagrangeInter(x_in, xarr, yarr):
    result = 0
    a = []
    for k in range(len(yarr)):
        lnx = 1
        for i in range(len(xarr)):
            if i != k:
                lnx *= (x_in - xarr[i]) / (xarr[k] - xarr[i])
        a.append(lnx)
    for i in range(len(yarr)):
        result += a[i] * yarr[i]
    return result


def calcDifferenceQuotient(xarr, yarr):
    D = len(xarr)
    table = np.zeros([D, D], dtype=float)
    for i in range(D):
        table[i][0] = yarr[i]
    for j in range(1, D):
        for i in range(j, D):  # i阶差商
            table[i][j] = (table[i][j - 1] - table[i - 1][j - 1]) / (xarr[i] - x[i - j])
    # print(table)
    return table


def newtonInter(x_in, xarr, yarr):
    QuotientTable = calcDifferenceQuotient(xarr, yarr)
    n = len(xarr)
    result = QuotientTable[0][0]
    for i in range(1, n):
        temp = 1
        for k in range(0, i):
            temp *= (x_in - xarr[k])
        result += QuotientTable[i][i] * temp
    return result


if __name__ == '__main__':
    # data
    x = np.arange(0.4, 0.9, 0.1)
    y = np.array([-0.916291, -0.693147, -0.510826, -0.357765, -0.223144])

    # linear interpolation
    print("result of linear interpolation:", linearInter(0.54, x, y))

    # Newton interpolation
    print("result of newton interpolation:", newtonInter(0.54, x, y))

    # Lagrange interpolation
    print("result of lagrange interpolation:", lagrangeInter(0.54, x, y))

    # Quadratic interpolation
    print("result of quadratic interpolation:", quadraticInter(0.54, x, y))
