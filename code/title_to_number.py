class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Excel表列序号
        给定一个Excel表格中的列名称，返回其相应的列序号。
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...
        :param columnTitle:
        :return:
        """
        result = 0
        for character in columnTitle:
            result *= 26
            result += ord(character) - 64  # ord("A")=>65
        return result
