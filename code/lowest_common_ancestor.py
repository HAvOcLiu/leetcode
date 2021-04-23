# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉树的最近公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_stack = [root]
        path_dict = {root: None}

        # 先遍历一遍，建立一层父子关系
        while (p not in path_dict) or (q not in path_dict):
            current_node = node_stack.pop()
            if current_node.left:
                path_dict[current_node.left] = current_node
                node_stack.append(current_node.left)
            if current_node.right:
                path_dict[current_node.right] = current_node
                node_stack.append(current_node.right)

        # p的路径
        current_node = p
        path_p = [p]  # 认为自己也是自己的祖先节点
        while current_node in path_dict:
            path_p.append(path_dict[current_node])
            current_node = path_dict[current_node]

        # 公共祖先
        while q not in path_p:
            q = path_dict[q]
        return q
