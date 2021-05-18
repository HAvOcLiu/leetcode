from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        单词拆分
        给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

        说明：
            拆分时可以重复使用字典中的单词。
            你可以假设字典中没有重复的单词。

        :param s:
        :param wordDict:
        :return:
        """
        possible_break = [0]
        word_dict = set(wordDict)
        for i in range(len(s) + 1):
            for j in possible_break:
                if s[j:i] in word_dict:
                    possible_break.append(i)
                    break
        return possible_break[-1] == len(s)

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        word_dict = set(wordDict)
        for i in range(n):
            if s[:i + 1] in word_dict:
                dp[i] = True
            else:
                for j in range(i - 1, -1, -1):
                    if dp[j] and s[j + 1:i + 1] in word_dict:
                        dp[i] = True
                        break
        return dp[n - 1]
