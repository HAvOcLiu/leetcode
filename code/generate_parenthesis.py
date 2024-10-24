from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        括号生成
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
        :param n:
        :return:
        """
        result_set = {"()"}
        for i in range(1, n):
            new_result = set()
            for result in result_set:
                for j in range(len(result)):
                    new_result.add(result[:j] + "()" + result[j:])
            result_set = new_result
        return list(result_set)
