class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        删除链表的倒数第N个结点
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
        进阶：你能尝试使用一趟扫描实现吗？
        :param head:
        :param n:
        :return:
        """
        k = ListNode(0)  # 新建一个0号结点
        k.next = head  # 0号结点放在头结点前面
        p = head  # 初始化p，指向头结点
        q = k  # 初始化q，指向0号结点。也就是说p在q前面一个位置
        for _ in range(n):
            p = p.next  # 先把p向前移动n个位置，这时候p在q前面n+1个位置
        while p:
            p = p.next  # 再同时移动p和q，直至p遍历完整个链表。
            q = q.next  # 这个过程中p始终在q前面n+1个位置
        q.next = q.next.next  # q的下一个位置就是要删除的节点
        return k.next  # 0号结点的下一个位置是头结点
