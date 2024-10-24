class Solution:
    # 无重复字符的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        e.g.: s="abcbcab"
        i=0, j=3, sub_str="abc"
        此时我们选择让i跳过sub_str的中"b"的位置，即把sub_str更新成"c"。
        因为重复字符是"b"，如果i只前进一个字符，接下来还是会重复，而且sub_str更短。
        所以不如直接把这一段都跳过去。
        :param s:
        :return:
        """
        len_s = len(s)
        if len_s < 2:
            return len_s

        sub_str = {}
        i = 0
        result = 0
        for j in range(len_s):
            if s[j] in sub_str:
                i = max(sub_str.get(s[j]), i)
            result = max(result, j - i + 1)
            sub_str[s[j]] = j + 1  # 把字符s[j]的下一个位置放到字典，这样下次取出来赋值给i的时候，就跳过了字符s[j]
        return result
