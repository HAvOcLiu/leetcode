from collections import Counter


class Solution:
    # 最小覆盖子串
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t)  # 目标字符串构建一个字典 {字符：数量}
        required = len(dict_t)  # 目标字符串的长度
        left = 0  # 窗口右端
        right = 0  # 窗口左端
        formed = 0  # 已经解决的的字符数量
        window_counts = {}  # 窗口中的子串字典 {字符：数量}
        ans = float("inf"), None, None  # 答案三元组 (长度, 子串起始位置, 子串结束位置)

        filtered_s = []  # 过滤字符串s
        for i, character in enumerate(s):
            if character in dict_t:
                filtered_s.append((i, character))  # 只要目标字符串中有的，并记录位置

        # 初始时窗口左端和右端都在位置0
        # 窗口右端不断右移
        while right < len(filtered_s):
            character = filtered_s[right][1]  # 取出当前字符
            window_counts[character] = window_counts.get(character, 0) + 1  # 窗口里包含的当前字符数量+1

            if window_counts[character] == dict_t[character]:  # 如果窗口中当前字符的数量与目标字符串中这个字符的数量一致
                formed += 1  # 说明已经解决了一个字符

            # 以下，是在解决所有字符的情况下，不断左移窗口左端，尝试缩小子串长度的操作
            while left <= right and formed == required:
                start = filtered_s[left][0]
                end = filtered_s[right][0]
                if end - start + 1 < ans[0]:  # 如果长度比已知最小长度还要小
                    ans = (end - start + 1, start, end)  # 更新答案

                character = filtered_s[left][1]  # 当前字符
                left += 1  # 窗口左端左移一个位置
                window_counts[character] -= 1  # 因为左移了，把窗口里当前字符的数量-1
                if window_counts[character] < dict_t[character]:  # 字符数量对不上了
                    formed -= 1  # 解决的字符数-1
            # 缩小窗口的尝试结束
            # 窗口右端右移一个位置，尝试下一个字符
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
