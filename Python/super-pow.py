# 
# Time:  O(n), n is the size of b.
# Space: O(1)

# Your task is to calculate a^b mod 1337 where a is a positive integer
# and b is an extremely large positive integer given in the form of an array.
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024
# ab % k = ((a%k) * (b % k)) % k

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        #  a = a, b = 1337, n = ??
        def myPow(a, n, b):
            result = 1
            x = a % b
            while n:
                # n & 1 = n & 1, if n & 1 = if n != 0
                if n & 1:
                    result = result * x % b
                n >>= 1
                x = x * x % b
            return result % b

        result = 1
        for digit in b:
            result = myPow(result, 10, 1337) * myPow(a, digit, 1337) % 1337
        return result

    def superPow2(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        def myPow(a, n):
            result = 1
            a %= 1337
            while n:
                result = result * a % 1337

            return result

        if len(b) == 0:
            return 1
        last_digit = b.pop()
        print "last_digit:"+ format(last_digit)

        return myPow(self.superPow2(a, b), 10) * myPow(a, last_digit) % 1337



if __name__ == '__main__':
    print Solution().superPow(2, [1, 2, 3, 4])
    # print Solution().superPow2(2, [1, 2, 3, 4])
