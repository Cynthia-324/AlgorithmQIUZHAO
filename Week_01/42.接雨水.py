#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        l_max = r_max = 0
        sum_trap = 0
        while left<right:
                if height[left]<height[right]:
                    if height[left] < l_max:
                        sum_trap = sum_trap + l_max - height[left]
                    else :
                        l_max = height[left]
                    left += 1
                else:
                    if height[right] < r_max:
                        sum_trap = sum_trap + r_max - height[right]
                    else:
                        r_max = height[right]
                    right -= 1
        return sum_trap

# @lc code=end

