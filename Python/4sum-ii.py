# -*- coding: UTF-8 -*-
# Time:  O(n^2)
# Space: O(n^2)

# Given four lists A, B, C, D of integer values,
# compute how many tuples (i, j, k, l) there are
# such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        # a+b 各种组合的和及其数量
        # -c-d 是 （c+d)的负数，如果与A_B_sum,相等，则总和为0；
        # 从A_B_sum,这个（和:计数)字典中统计总计数，就是总的个数
        return sum(A_B_sum[-c-d] for c in C for d in D)

if __name__ == '__main__':
    print Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
