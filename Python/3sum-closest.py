# -*- coding: UTF-8 -*-
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# 给一个array S，查找三个实数，其和接近一个给定的数字
# find three integers in S such that the sum is closest to a given number, target.
# 返回三和数字的和
# Return the sum of the three integers.
# 假设每个输入都只有一个输出
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
        print result
        print min_diff
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff < 0:
                        j += 1
                    elif diff > 0:
                        k -= 1
                    else:
                        return target
            i += 1
        return result

if __name__ == '__main__':
    result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print result
