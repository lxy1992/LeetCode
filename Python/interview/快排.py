"""
最好O(N)
平均情况 O(N*LogN)   分割或者递归一般都是这个复杂度
最坏O(N^2)

空间复杂度：最好O(logN)
最坏：O(n)

这应该是一个非原地版本，原地版本一般用C来写，可以降低空间复杂度
"""
def qsort(seq):
    if not seq:
        return []
    else:
        pivot = seq[0]
        lesser = qsort([x for x in seq[1:] if x < pivot])
        greater = qsort([x for x in seq[1:] if x >= pivot])
        return lesser+[pivot]+greater

if __name__=='__main__':
    seq = [5,6,78,9,0,-1,2,3,-65,12]
    print(qsort(seq))