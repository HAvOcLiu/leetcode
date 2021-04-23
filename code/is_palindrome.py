class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        验证回文串
        给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
        :param s:
        :return:
        """
        if not s:
            return True  # 本题中，我们将空字符串定义为有效的回文串
        s_lower = s.lower()
        import re
        pattern = re.compile("[^a-z0-9]")
        s_lower = pattern.sub("", s_lower)
        i = 0
        j = len(s_lower) - 1
        while i < j:
            if s_lower[i] != s_lower[j]:
                return False
            i += 1
            j -= 1
        return True
