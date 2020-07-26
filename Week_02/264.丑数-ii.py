#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 7:
            return n
        arr = [1 for _ in range(n)]
        p2, p3, p5 = 0, 0, 0
        for i in range(1,n):
            minval = min(arr[p2]*2,arr[p3]*3,arr[p5]*5)
            arr[i] = minval
            if arr[p2]*2 == minval:
                p2 += 1
            if arr[p3]*3 == minval:
                p3 += 1
            if arr[p5]*5 == minval:
                p5 += 1
        return arr[-1]


# @lc code=end

