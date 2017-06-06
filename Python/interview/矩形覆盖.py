# -*- coding: UTF-8 -*-

# 我们可以用 2*1 的小矩形横着或者竖着去覆盖更大的矩形。请问用n个 2*1 的小矩形无重叠地覆盖
# 一个 2*n 的大矩形，总共有多少种方法?
f = lambda n: 1 if n < 2 else f(n - 1) + f(n - 2)


def memo(fun):
    cache = {}
    def wrap(*kwags):
        if kwags not in cache:
            cache[kwags] = fun(*kwags)
        return cache[kwags]
    return wrap

@memo
def rect(n):
    if n < 2:
        return 1
    else:
        return rect(n-1) + rect(n-2)


if __name__ == '__main__':
    n = 10
    print rect(10)