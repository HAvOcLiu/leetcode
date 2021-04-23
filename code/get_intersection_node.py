class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        编写一个程序，找到两个单链表相交的起始节点。
        """
        p = headA
        q = headB
        while True:
            if p == q:
                return p
            else:
                if p:
                    p = p.next
                else:
                    p = headB

                if q:
                    q = q.next
                else:
                    q = headA
