# coding: utf-8

a = [4,2,5,3,1,8,20,31,24,35,6]

print 'before sort', a[:]

def mergeSort(array, p, q, r):
    L = []
    R = []
    n1 = q-p+1
    n2 = r-q
    for i in xrange(p, q+1):
        L.append(array[i])
    for j in xrange(q+1, r+1):
        R.append(array[j])