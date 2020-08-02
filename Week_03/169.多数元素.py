#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        '''
        count = 0
        candidate = None


        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)


        return candidate
# @lc code=end

