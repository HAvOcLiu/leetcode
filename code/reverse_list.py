# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        反转链表
        给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
        :param head:
        :return:
        """
        p = None
        q = head
        while q:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        return p
