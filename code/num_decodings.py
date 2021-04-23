class Solution:
    def numDecodings(self, s: str) -> int:
        """
        解码方法
        一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
            'A' -> 1
            'B' -> 2
            ...
            'Z' -> 26
        要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
        例如，"11106" 可以映射为：
            "AAJF" ，将消息分组为 (1 1 10 6)
            "KJF" ，将消息分组为 (11 10 6)
        注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
        给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
        题目数据保证答案肯定是一个 32 位 的整数。

        :param s:
        :return:
        """
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        magic_set = {"10", "20"}
        a = 1
        if s[:2] in magic_set:
            b = 1
        elif 11 <= int(s[:2]) <= 26:
            b = 2
        else:
            if int(s[1]) == 0:
                return 0
            b = 1

        for i in range(2, len(s)):
            if s[i] != "0":
                if 11 <= int(s[i - 1:i + 1]) <= 26:
                    c = a + b
                else:
                    c = b
            else:
                if s[i - 1:i + 1] in magic_set:
                    c = a
                else:
                    return 0
            a = b
            b = c
        return b
