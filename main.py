"""Демомодуль для курса. Eval Loop"""

import dis


def pr(a):
    return a + 1


def sum_new(a, b):
    c = a + b
    d = pr(c)
    return d


x = sum_new(1, 2)

dis.dis(sum_new)
