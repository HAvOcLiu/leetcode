# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 验证二叉搜索树
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = []
        pre_val = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= pre_val:
                return False
            pre_val = root.val
            root = root.right

        return True
