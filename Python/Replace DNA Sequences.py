# coding=utf-8
## 给定两条DNA序列，测试两个长度相等的序列是否碱基配对，不配对的可以通过替换配对，返回最少替换次数


import sys

if __name__ == '__main__':
    DNA = str(sys.stdin.readline().strip())
    DNA2 = DNA.split(' ')
    D1 = DNA2[0]
    D2 = DNA2[1]
    c = 0
    for i in xrange(1, len(D1)):
        print i
        if D1[i] is 'A' and D2[i] is not 'T':
            c += 1
        if D1[i] is 'T' and D2[i] is not 'A':
            c += 1
        if D1[i] is 'C' and D2[i] is not 'G':
            c += 1
        if D1[i] is 'G' and D2[i] is not 'C':
            c += 1
    print c



