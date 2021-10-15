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
    returns = (returns[0] // gcd_, returns[1] // gcd_)
    return returns


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
    returns = (returns[0] // gcd_, returns[1] // gcd_)
    return returns


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
    returns = (returns[0] // gcd_, returns[1] // gcd_)
    return returns


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
    returns = (returns[0] // gcd_, returns[1] // gcd_)
    return returns


print(divide(-1, 10, 2, 5))
