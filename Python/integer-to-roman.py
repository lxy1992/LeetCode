# Time:  O(n): 162ms
# Space: O(1)
#
# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#


class Solution:
    # @return a string
    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(numeral_map.keys()), ""
        
        while num > 0:
            for key in reversed(keyset):
                while num / key > 0:
                    num -= key
                    result += numeral_map[key]
                    
        return result

    # Time: O(1): 95ms
    # Space: O(1)
    def intToRoman2(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];

if __name__ == "__main__":
    print Solution().intToRoman(999)
    print Solution().intToRoman(3999)
    print Solution().intToRoman2(999)
    print Solution().intToRoman2(3999)