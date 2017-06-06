import math


def calGCD(op1, op2):
    if (op2 == 0):
        return op1
    else:
        return calGCD(op2, op1 % op2)

list = [1,2,]
temp = list
n = len(list)
res = calGCD(list[1], list[0])
list.pop(0)
list.pop(0)

for i in xrange(n-3):
    res = calGCD(res, list[i])
print res
for i in temp:
    res /= i
print res
print math.log(res, 2)