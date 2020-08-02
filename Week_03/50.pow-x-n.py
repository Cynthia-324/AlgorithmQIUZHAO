#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """    
        def quickmul(x,n):
            if n == 0:
                return 1.0
            res = quickmul(x,n//2)
            return  res * res if n % 2 == 0 else res * res * x
        
        return quickmul(x,n) if n >= 0 else 1.0/quickmul(x,-n)
            
# @lc code=end

