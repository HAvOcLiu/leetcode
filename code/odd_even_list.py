# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 奇偶链表
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next):
            return head

        p = head
        h2 = p.next
        q = h2

        while True:
            p.next = q.next
            if not p.next:
                p.next = h2
                break
            p = p.next
            q.next = p.next
            if not q.next:
                p.next = h2
                break
            q = q.next
        return head
