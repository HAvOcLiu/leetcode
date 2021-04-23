from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 从先序和中序遍历结果还原二叉树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        stack = []  # 使用一个栈
        root_node = TreeNode(preorder[0])  # 先序遍历的第一个就是树的根节点
        stack.append(root_node)  # 根节点入栈

        # 处理后续节点
        # i是preorder数组的下标
        # j是inorder数组的下标
        j = 0
        for i in range(1, len(preorder)):
            current_node = TreeNode(preorder[i])  # 从preorder里依次取值，作为当前节点
            back = None  # 回溯用的节点
            # 如果中序的节点不在栈顶，那么当前节点就是栈顶元素的左孩子节点
            # 如果中序的节点在栈顶，那么回溯，直到中序元素不在栈顶，这时当前节点就是回溯节点的右孩子节点
            # 最后把当前节点入栈
            while len(stack) > 0 and stack[len(stack) - 1].val == inorder[j]:
                back = stack.pop()
                j += 1
            if back:
                back.right = current_node
            else:
                stack[len(stack) - 1].left = current_node
            stack.append(current_node)
        return root_node
