# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

        # 回文链表

    def isPalindromeList(self, head: ListNode) -> bool:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        if n < 2:
            return True  # 空的和只有一个的也认为是回文链表，智障

        i = 0
        n_half = n // 2
        if n % 2 == 0:
            n_half -= 1  # 偶数的情况要少反向一次
        p = head
        q = head.next
        head.next = None
        while i < n_half:
            t = q.next
            q.next = p
            p = q
            q = t
            i += 1

        if n % 2 != 0:
            p = p.next  # 奇数的情况下往后走一个，对齐
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
