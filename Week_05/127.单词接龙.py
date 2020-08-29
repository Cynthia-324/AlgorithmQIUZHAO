#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #set 方便快速查找
        word_set = set(wordList)
        if (len(word_set) == 0) or endWord not in word_set:
            return 0
        #查找集中删除初始单词
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()
                word_list = list(word)

                #创建连通图
                for j in range(word_len):
                    origin_char = word_list[j]
                    
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        #如果单词在字典中
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0
        
# @lc code=end

