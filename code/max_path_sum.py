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
        同一个节点在一条路径序列中 至多出现一次 。
        该路径 至少包含一个 节点，且不一定经过根节点。
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

    def maxPathSum_non_recursive(self, root: TreeNode) -> int:
        """
        二叉树中的最大路径和
        路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
        同一个节点在一条路径序列中 至多出现一次 。
        该路径 至少包含一个 节点，且不一定经过根节点。
        路径和 是路径中各节点值的总和。
        给你一个二叉树的根节点 root ，返回其 最大路径和 。

        :param root:
        :return:
        """
        max_sum = -sys.maxsize - 1  # 初始化最大路径和为系统最小值
        if not root:
            return 0  # 不处理空树

        # 双栈法后序遍历二叉树
        stack_sum = []
        stack_tmp = [root]  # 根节点直接入栈
        while stack_tmp:
            tmp = stack_tmp.pop()  # 出栈一个节点
            stack_sum.append(tmp)  # 加入另一个栈
            if tmp.left:
                stack_tmp.append(tmp.left)  # 如果有左孩子节点，左孩子节点入栈
            if tmp.right:
                stack_tmp.append(tmp.right)  # 如果有右孩子节点，右孩子节点入栈

        # stack_sum栈中的节点依次出栈即可得到后序遍历的结果
        # 后续遍历的特点是最后访问根节点
        # 在访问过程中逐次更新每个节点的值
        # 这相当于一个从叶子结点开始，逐渐向上累积的过程
        while stack_sum:
            tmp = stack_sum.pop()  # 出栈一个节点
            max_sum = max(max_sum, tmp.val)  # 如果这个节点的值比当前的最大路径和要大，就让这个大的值成为最大路径和
            left = 0  # 初始化当前节点的左子树收益为0
            if tmp.left:
                left = max(tmp.left.val, left)  # 如果当前节点有左孩子节点，根据左孩子节点的值，更新左子树的收益
            right = 0  # 初始化当前节点的右子树收益为0
            if tmp.right:
                right = max(tmp.right.val, right)  # 如果当前节点有右孩子节点，根据右孩子节点的值，更新右子树的收益
            # 一条从当前节点左子树经过当前节点到当前节点右子树的路径
            # 基于上面的计算，这条路径代表了能够取得最大收益的那条
            # 计算路径和
            tmp_sum = tmp.val + left + right
            # 当前节点的值更新成最大收益的那条路径
            # 可能是左边，可能是右边，也可能两边都不要
            # 但是不能两边都选，因为路径不允许这样
            tmp.val += max(left, right)
            max_sum = max(max_sum, tmp_sum)  # 新的路径和比较大，更新最大路径和

        return max_sum
