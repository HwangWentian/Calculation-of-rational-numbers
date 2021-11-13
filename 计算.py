from math import gcd

"""
实现对实数的精密计算，返回值为一个二元组 (molecular, denominator)，表示结果为 molecular / denominator
"""


def add(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """
    :param a1: 第一个加数的分子
    :param b1: 第一个加数的分母
    :param a2: 第二个加数的分子
    :param b2: 第二个加数的分母
    :return: 运算结果的分子和分母，形式为 ({分子}, {分母})
    """
    gcd_ = b1 * b2 // gcd(b1, b2)
    a1 *= gcd_ // b1
    a2 *= gcd_ // b2
    returns = [a1 + a2, gcd_]
    gcd_ = gcd(returns[0], returns[1])
    return returns[0] // gcd_, returns[1] // gcd_


def subtract(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """
    :param a1: 被减数的分子
    :param b1: 被减数的分母
    :param a2: 减数的分子
    :param b2: 减数的分母
    :return: 运算结果的分子和分母，形式为 ({分子}, {分母})
    """
    gcd_ = b1 * b2 // gcd(b1, b2)
    a1 *= gcd_ // b1
    a2 *= gcd_ // b2
    returns = [a1 - a2, gcd_]
    gcd_ = gcd(returns[0], returns[1])
    return returns[0] // gcd_, returns[1] // gcd_


def multiply(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """
    :param a1: 第一个因数的分子
    :param b1: 第一个因数的分母
    :param a2: 第二个因数的分子
    :param b2: 第二个因数的分母
    :return: 运算结果的分子和分母，形式为 ({分子}, {分母})
    """
    returns = [a1 * a2, b1 * b2]
    gcd_ = gcd(returns[0], returns[1])
    return returns[0] // gcd_, returns[1] // gcd_


def divide(a1: int, b1: int, a2: int, b2: int) -> tuple:
    """
    :param a1: 被除数的分子
    :param b1: 被除数的分母
    :param a2: 除数的分子
    :param b2: 除数的分母
    :return: 运算结果的分子和分母，形式为 ({分子}, {分母})
    """
    returns = [a1 * b2, b1 * a2]
    gcd_ = gcd(returns[0], returns[1])
    return returns[0] // gcd_, returns[1] // gcd_


def power(a1: int, a2: int, b: int) -> tuple:
    """
    :param a1: 底数的分子
    :param a2: 底数的分母
    :param b: 指数（为整数）
    :return: 运算结果的分子和分母，形式为 ({分子}, {分母})
    """
    n = 1
    m = 1
    for i in range(abs(b)):
        n *= a1
        m *= a2
    gcd_ = gcd(n, m)
    if b < 0:
        return m // gcd_, n // gcd_
    else:
        return n // gcd_, m // gcd_


print(power(3, 1, -2))
