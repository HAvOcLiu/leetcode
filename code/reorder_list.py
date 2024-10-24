from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        143. 重排链表
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        print("mid.val:{}".format(mid.val))
        head2 = self.reverseList(mid)
        print("head2.val:{}".format(head2.val))
        head1 = head
        print("head1.val:{}".format(head))
        while head2.next:
            nxt1 = head1.next
            nxt2 = head2.next
            head1.next = head2
            head2.next = nxt1
            head1 = nxt1
            head2 = nxt2
            
            test_head = head
            values = []
            while test_head:
                values.append(test_head.val)
                test_head = test_head.next
            print(values)


solution = Solution()
head = ListNode(1)
p = head
for i in range(2,5):
    new_node = ListNode(i)
    p.next = new_node
    p = new_node

test_head = head
values = []
while test_head:
    values.append(test_head.val)
    test_head = test_head.next
print(values)

solution.reorderList(head)
