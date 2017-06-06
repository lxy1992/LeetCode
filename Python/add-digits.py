# -*- coding: UTF-8 -*-
# Time:  O(1)
# Space: O(1)
#
# Given a non-negative integer num, repeatedly add
# all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11,
# 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1)
# runtime?
#
# Hint:
#
# A naive implementation of the above process is trivial.
# Could you come up with other methods? 


class Solution:
    """
    :type num: int
    :rtype: int
    """
    def addDigits(self, num):
        # 主要依据来自：
        # 1. 987654321 = 9 * 10^9 + 8 * 10 ^ 8 +...+1
        # 2. 1, 10, 100, 1000...% 9 = 1
        # 3. (a + b) % 9 = (a%9 + b%9)%9
        # 4. 因此，num % 9 = 各位递归和
        # 5. 为了解决 9 % 9 = 0,而不是应该输出的9，采用了 (n-1)%9 + 1的办法
        return (num - 1) % 9 + 1 if num > 0 else 0


if __name__ == '__main__':
    s = Solution()
    r = s.addDigits(12345)
    print r
