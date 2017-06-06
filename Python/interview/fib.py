# -*- coding: UTF-8 -*-
"""计算斐波那契数列和"""
# 递归方式实现
# 调用次数呈指数级增长
fib_re = lambda n: n if n <= 2 else fib_re(n - 1) + fib_re(n - 2)
    

# 装饰器实现
# 使用装饰器实现一个缓存的作用
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib_cache(i):
    if i < 2:
        return 1
    return fib_cache(i-1) + fib_cache(i-2)


# 使用动态规划
def fib_dy(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b


 # 变态台阶问题 一只青蛙一次可以跳上1级台阶，也可以跳上2级... ...它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


fib_n = lambda n: n if n < 2 else 2 * fib_n(n - 1)


"""打印斐波那契数列"""
# 线性增长的斐波那契数列
def fib_dy_p(n):
    a, b = 0, 1
    result = []
    for _ in xrange(n):
        result.append(b)
        a, b = b, a+b
    return result

# 使用生成器函数实现，其实也是协程
def fib_ye(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1


def fib3_cache_print(n, cache={0: 1, 1: 1}):
    """Fib with recursion and caching."""

    try:
        return cache[n]
    except KeyError:
        cache[n] = fib3_cache_print(n-1) + fib3_cache_print(n-2)
        # print cache[n]
        return cache[n]


if __name__ == '__main__':
    n = 10
    print "求取 %s 位斐波那契数列的和" %n
    print fib_re(n)
    print "========="
    print fib_cache(n)
    print "========="
    print fib_dy(n)
    print "========="
    print fib3_cache_print(n)
    print "打印 %s 位斐波那契数列" %n
    print fib_dy_p(n)
    print "========="
    for _ in fib_ye(n):
        print _
    print "========="