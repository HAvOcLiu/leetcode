# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 填充每个节点的下一个右侧节点指针
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            current_node = leftmost
            while current_node:
                if current_node.left is not None:
                    current_node.left.next = current_node.right
                if current_node.next is not None:
                    current_node.right.next = current_node.next.left
                current_node = current_node.next
            leftmost = leftmost.left

        return root
