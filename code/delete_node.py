class Solution:
    def deleteNode(self, node):
        """
        删除链表中的节点
        请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。
        传入函数的唯一参数为 要被删除的节点 。
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
