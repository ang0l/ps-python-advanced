"""Демомодуль для курса. Память и сборка мусора"""

# import sys


# a = [1, 2, 3]
# b = a
# del a
# print(b)
# print(sys.getrefcount(b))

import gc


a = []
b = [a]
a.append(b)

print(gc.get_stats())
gc.collect()
