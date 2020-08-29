#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        result = [1,2]
        
        while n > 2:
            result.append(result[-1]+result.pop(0)) 
            n -= 1
        return result[-1] 
# @lc code=end

