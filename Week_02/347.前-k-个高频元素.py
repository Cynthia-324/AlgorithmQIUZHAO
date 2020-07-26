#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        record = Counter(nums)
        heap = []
        res = []
        for num,freq in record.items():
            if len(heap)== k:
                if heap[0][0] < freq:
                    heapq.heapreplace(heap,(freq,num))
            else :
                heapq.heappush(heap,(freq,num))
        while heap:
            res.append(heapq.heappop(heap)[1])
        res = res[::-1]
        return res

# @lc code=end

