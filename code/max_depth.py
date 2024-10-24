# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return result

        queue = [(root, 1)]
        while queue:
            (current_node, depth) = queue.pop(0)
            result = max(result, depth)

            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))
        return result
