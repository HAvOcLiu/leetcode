from typing import List


class Solution:
    # 分割回文串
    def partition(self, s: str) -> List[List[str]]:
        """
        两种情况：
            1. 新加入的字符与前一个元素组成回文串，那么这两个元素单独拆出来，作为一个新的可行结果
            2. 新加入的字符与前两个元素组成回文串，那么这三个元素单独拆出来，作为一个新的可行结果
        如果新加入的字符与前三个元素组成回文串，那么这四个元素中间的两个元素一定是回文的，转到第一种情况。
        如果新加入的字符与前四个元素组成回文串，那么这五个元素中间的三个元素一定是回文的，转到第二种情况。
        以此类推，我们只要处理两种情况就好了。
        :param s: 待分割的字符串
        :return: 所有可行的分割结果
        """
        if not s:
            return [[]]

        candidates = [[s[0]]]  # 保存所有可行的结果，默认放入第一个字符
        for i in range(1, len(s)):  # 从第二个字符开始，遍历后续所有字符
            for candidate in candidates[:len(candidates)]:  # 遍历上一轮增加一个字符之后所有的可行分割方案
                if len(candidate) > 1 and s[i] == candidate[-2]:  # 第二种情况
                    # 生成一个新的可行分割方案
                    candidates.append(candidate[:-2] + [candidate[-2] + candidate[-1] + s[i]])  # 注意这里第二部分中括号里是字符拼接成字符串
                if s[i] == candidate[-1]:  # 第一种情况
                    candidates.append(candidate[:-1] + [candidate[-1] + s[i]])
                candidate.append(s[i])
        return candidates
