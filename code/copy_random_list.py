class Node:
    """
    Definition for a Node.
    """

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        复制带随机指针的链表
        给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
        构造这个链表的深拷贝。深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。
        新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。
        复制链表中的指针都不应指向原链表中的节点 。
        例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
        返回复制链表的头节点。

        :param head:
        :return:
        """
        if not head:
            return head  # 空链表

        visited_node = {}  # 复制过的节点，key:old_node，value:new_node

        old_node = head
        new_node = Node(old_node.val)
        visited_node[old_node] = new_node

        while old_node:
            # 处理next指针
            tmp_node = old_node.next
            if tmp_node:
                if tmp_node in visited_node:
                    new_node.next = visited_node[tmp_node]
                else:
                    visited_node[tmp_node] = Node(tmp_node.val)
                    new_node.next = visited_node[tmp_node]
            else:
                new_node.next = None

            # 处理random指针
            tmp_node = old_node.random
            if tmp_node:
                if tmp_node in visited_node:
                    new_node.random = visited_node[tmp_node]
                else:
                    visited_node[tmp_node] = Node(tmp_node.val)
                    new_node.random = visited_node[tmp_node]
            else:
                new_node.random = None

            # 下一个
            old_node = old_node.next
            new_node = new_node.next
        return visited_node[head]
