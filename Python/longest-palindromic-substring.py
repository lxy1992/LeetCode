# Time:  O(n)
# Space: O(n)
#
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#

# Manacher's Algorithm
# http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Convert the origial string into an even string by adding #, ^, $
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for c in s:
                T += ['#', c]
            T += ['#', '$']
            return T

        # T is the coverted string
        T = preProcess(s)
        # Creat a all-0 list whose length equal to T
        # T is to store the max radio length of current string in T
        P = [0] * len(T)
        # 'center' is the temporal known longest palindromic substring
        # 'right' is the right boundary of this substring
        center, right = 0, 0
        for i in xrange(1, len(T) - 1):
            # Based on center, find the mirror i
            i_mirror = 2 * center - i
            # When temporal best right boundary larger than current i
            # Which means a part of current substring is in the temporal best palindromic substring
            # This if..else part is aimed to save some calculations of the P[i], based on the fundamental of palindromic string and mirror string by finding the most possible start value of P[i]
            if right > i:
                #
                P[i] = min(right - i, P[i_mirror])
            else:
                P[i] = 0
            # Using the fundamental of while to find the real P[i] based on the strat P[i]
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # If the right boundary of new P[i] larger than current 'right', update the 'center' and 'right'.
            if i + P[i] > right:
                center, right = i, i + P[i]
                # find the start-end index of the longest palindromic substring.
        max_i = 0
        for i in xrange(1, len(T) - 1):
            if P[i] > P[max_i]:
                max_i = i
        start = (max_i - 1 - P[max_i]) / 2
        return s[start: start + P[max_i]]


if __name__ == "__main__":
    print Solution().longestPalindrome("abb")
