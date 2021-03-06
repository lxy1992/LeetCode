# Time:  O(n * l^2)
# Space: O(n)

# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)

        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))

        can_break = [False for _ in xrange(n + 1)]
        can_break[0] = True
        for i in xrange(1, n + 1):
            for l in xrange(1, min(i, max_len) + 1):
                if can_break[i-l] and s[i-l:i] in wordDict:
                    can_break[i] = True
                    break

        return can_break[-1]

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l1 = len(s)
        print 'length of s:' + format(l1)
        rtype = ''
        str = ''
        for i in s:
            rtype += i
            s = s[1:]
            print 's:' + format(s)
            if rtype in wordDict:
                print 'rtype:' + format(rtype)
                str += rtype
                rtype = ''
        print 'str:' + format(str)
        print 'length of str:' + format(len(str))
        return bool(len(str) == l1)

    
if __name__ == "__main__":
    print Solution().wordBreak2("leetcode", ["leet", "code"])
    print Solution().wordBreak2("aaaaaaa", ["aaaa", "aaa"])
