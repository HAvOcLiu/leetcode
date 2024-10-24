# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 两数相加
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        head = ListNode(0)
        result = head
        add = 0

        while True:
            new_node = False
            result.val = l1.val + l2.val + add
            if result.val > 9:
                result.val = result.val - 10
                add = 1
            else:
                add = 0

            if l1.next:
                l1 = l1.next
                new_node = True
            else:
                l1.val = 0

            if l2.next:
                l2 = l2.next
                new_node = True
            else:
                l2.val = 0

            if new_node:
                next_node = ListNode(0)
                result.next = next_node
                result = result.next
            elif add > 0:
                next_node = ListNode(add)
                result.next = next_node
                break
            else:
                break
        return head
