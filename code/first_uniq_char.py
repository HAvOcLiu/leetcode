class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        字符串中的第一个唯一字符
        给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
        :param s:
        :return:
        """
        char_set = set(s)
        passed_char_set = set()
        for character in s:
            if character in passed_char_set:
                if character in char_set:
                    char_set.remove(character)
            else:
                passed_char_set.add(character)
        if not char_set:
            return -1
        for i in range(len(s)):
            if s[i] in char_set:
                return i
