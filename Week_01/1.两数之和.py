#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #hashmap
        hashmap = {}
        for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index 
        return []
        
# @lc code=end

