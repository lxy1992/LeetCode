# -*- coding: UTF-8 -*-
import os
import timeit

"""1到100依次去掉偶数项求最后剩的俩数是什么？"""
def remove_non_odd(n):
    __l = []
    for ind, i in enumerate(n):
        if (ind+1) % 2 != 0:
            __l.append(i)
    return __l


def func(start, end):
    l = [x for x in range(start, end+1)]
    while len(l) > 2:
        l = remove_non_odd(l)
    # sum_last = l[0] + l[1]
    print l
    # print sum_last

# def remov(ind,i,l):
#
#     while i > 2:
#         print i
#         i = i / 2 + 1
#         if i % 2 == 0:
#             l.remove(ind)
#             break
#     return l
#
# def func2(start, end):
#     l = [x for x in range(start, end + 1)]
#     print l
#     for ind, i in enumerate(l):
#         print "ind: %s, i: %s" %(ind, i)
#         l = remov(ind, i, l)
#         # print l
#     print l
from math import log
def func2(nums, target):
    times = int(log(nums, 2))

    for i in xrange(times):
        target = target * 2 - 1
    res = []
    res.append(target)
    res.append(1)
    print res

if __name__ == '__main__':

