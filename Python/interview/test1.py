import itertools
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum, sum1, sum2 = 0, 1, 1
        for i in xrange(len(num1)-1,0,-1):
            n1 = 10 ^ (len(num1)-i)
            sum1 += (num1[i]*n1)
        for j in xrange(len(num2)-1,0,-1):
            n2 = 10 ^ (len(num2)-j)
            sum2 += (num2[j]*n2)
        sum = sum1 + sum2
        return sum

    def addStrings2(self, num1, num2):
        z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
        return (i[0] for i in z)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = 0
        for x in xrange(1, len(prices)):
            max_ending_here = max(0, max_ending_here += (prices[x] - prices[x - 1]))
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


if __name__ == '__main__':
    num1 = "999999"
    num2 = "99"
    s = Solution()
    print s.addStrings2(num1, num2)
