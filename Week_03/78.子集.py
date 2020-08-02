#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        #开始假设输出子集为空，每一步都向子集添加新的整数
        #并生成新的子集
        res = []
        def dfs(nums,start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(nums,i+1,path)
                path.pop()
        
        dfs(nums,0,[])
        return res
        '''
        #考虑长度为K的所有子集
        res = []
        def backtrack(first = 0,curr = []):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return res
            
# @lc code=end

