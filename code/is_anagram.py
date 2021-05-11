class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        有效的字母异位词
        给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
        :param s:
        :param t:
        :return:
        """
        char_count_dict = {}
        for char in s:
            char_count_dict[char] = char_count_dict.get(char, 0) + 1

        for char in t:
            if char not in char_count_dict:
                return False
            char_count_dict[char] = char_count_dict[char] - 1
            if char_count_dict[char] < 0:
                return False

        for char in char_count_dict:
            if char_count_dict[char] > 0:
                return False
        return True
