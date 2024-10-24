class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        正则表达式匹配
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

        :param s:
        :param p:
        :return:
        """
        result_matrix = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        result_matrix[0][0] = True
        # deals with patterns like a* or a*b* or a*b*c*
        for i in range(1, len(result_matrix[0])):
            if p[i - 1] == "*":
                result_matrix[0][i] = result_matrix[0][i - 2]

        for i in range(1, len(result_matrix)):
            for j in range(1, len(result_matrix[0])):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    result_matrix[i][j] = result_matrix[i - 1][j - 1]
                elif p[j - 1] == "*":
                    result_matrix[i][j] = result_matrix[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        result_matrix[i][j] = result_matrix[i][j] or result_matrix[i - 1][j]

        return result_matrix[len(s)][len(p)]
