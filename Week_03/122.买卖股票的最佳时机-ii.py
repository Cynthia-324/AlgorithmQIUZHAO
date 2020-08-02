#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        #贪心算法
        if prices <= 1: return 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
        '''
        '''
        #递归+记忆化
        if not prices:
            return 0
        n = len(prices)
        d = dict()
        #status = 0 已经卖出 status = 1 已经买入
        def dfs(index,status):
            if (index,status) in d:
                return d[index,status]
            if index == n:
                return 0
            a,b,c = 0,0,0
            #[不动]
            a = dfs(index+1,status)
            if status:
                #递归处理卖的情况
                b = dfs(index+1,0) + prices[index]
            else:
                #递归处理买的情况
                c = dfs(index+1,1) - prices[index]
            d[index,status] = max(a,b,c)
            return d[index,status]
        return dfs(0,0)
        '''
        #动态规划 dp[i][0] 第i天卖出的最大利润
        #dp[i][1] 第i天买入的最大利润
        if not prices: 
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        #初始化第1天
        dp[0][0] = 0
        dp[0][-1] = -prices[0]
        for i in range(1,n):
            #第i天卖出：第i-1天卖出，或者第i-1天买入，第i天卖出
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            #第i天买入：第i-1天买入，或者第i-1天卖出，第i天买入
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]

   
# @lc code=end

