from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        串联所有单词的子串
        给定一个字符串 s 和一些长度相同的单词 words。
        找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
        注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

        :param s: 给定的字符串
        :param words: 一些长度相同的单词
        :return: s中恰好可以由words中所有单词串联形成的子串的起始位置
        """
        # 把words转换成dict
        # key是words里的单词， value是这个单词在words里出现的次数
        word_count_dict = {}
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

        start_list = []  # 记录所有可以匹配的起始点
        len_s = len(s)  # 字符串s的长度
        num_words = len(words)  # words里面共有多少个单词
        len_word = len(words[0])  # words里的每个单词的长度

        for i in range(0, len_word):
            # 最多只有len_word种可以尝试的起点
            # 因为相差一个单词及以上的位置，在整个匹配过程中就会被检查到
            # 我们使用一个滑动的窗口，力求在窗口范围里匹配到一个合格的子串
            left = i  # 窗口左边界
            right = i  # 窗口右边界
            find_word_count = {}  # 匹配上的单词和对应的数量
            current_count = 0  # 已经匹配上的单词数量
            while right + len_word <= len_s:
                # 窗口的最大的右边界就在 right+len_word=len_s 的时候
                # 因为我们切一个单词使用 right+len_word 作为单词的右边界
                word = s[right:right + len_word]  # 切出一个单词
                # 右边界向右移动一个单词的长度
                # 到这个切出来的单词后面，使它进入窗口范围
                right += len_word
                if word not in word_count_dict:
                    # 如果切出来的单词匹配不上
                    # 所有包含这个单词的子串都不可能匹配上
                    # 我们需要跳过这个单词，重新匹配
                    left = right  # 左边界也跳到这个单词后面
                    find_word_count = {}  # 之前匹配的结果全部清空
                    current_count = 0  # 已经匹配上的单词数量也清零
                else:
                    # 匹配到一个单词
                    find_word_count[word] = find_word_count.get(word, 0) + 1  # 记录下来
                    current_count += 1
                    while find_word_count[word] > word_count_dict[word]:
                        # 单词虽然匹配上了，但是这个单词的数量超了
                        # 把左边界一直右移，直到单词数量不超为止
                        # 这个过程中需要把已经匹配上的部分移除一些
                        left_word = s[left:left + len_word]  # 最左面匹配过的单词
                        left += len_word  # 左边界右移一个单词的位置
                        find_word_count[left_word] -= 1  # 这个单词已经不在窗口范围里了，从匹配结果中删除
                        current_count -= 1  # 匹配上的单词总数也随之减一
                        # 这个循环过程我们是向右移动窗口的左边界
                        # 最多就移到和右边界差一个单词长度的位置
                        # 因为至少会保留一个单词在 find_word_count 里面
                        # 不会全清零
                    if current_count == num_words:
                        # 匹配上的单词数量等于words里单词数量
                        # 找到了一个合适的匹配结果
                        start_list.append(left)  # 把起点，也就是窗口的左边界，记录下来
        return start_list
