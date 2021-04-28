import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._max_sum = -sys.maxsize - 1

    def maxPathSum(self, root: TreeNode) -> int:
        """
        二叉树中的最大路径和
        路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
        同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
        路径和 是路径中各节点值的总和。
        给你一个二叉树的根节点 root ，返回其 最大路径和 。

        :param root:
        :return:
        """
        self._path_sum(root)
        return self._max_sum

    def _path_sum(self, node: TreeNode):
        if not node:
            return 0
        left = max(0, self._path_sum(node.left))
        right = max(0, self._path_sum(node.right))
        self._max_sum = max(self._max_sum, left + right + node.val)
        return max(left, right) + node.val
