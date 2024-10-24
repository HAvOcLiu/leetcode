# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 对称二叉树
    def isSymmetric(self, root: TreeNode) -> bool:
        # 层次遍历
        # 让这棵树自己照镜子
        queue = [root, root]

        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)  # 每次取两个值照镜子
            if not t1 and not t2:  # 全是空，认为相等，继续
                continue
            elif not t1 or not t2:  # 不全是空，一个空一个不空，就不相等了
                return False
            elif t1.val != t2.val:  # 全都不空，但是值不一样，还是不相等
                return False
            # 剩下的情况都相等
            queue.append(t1.left)
            queue.append(t2.right)  # 左右轴对称，连着放，取的时候连着取

            queue.append(t1.right)
            queue.append(t2.left)
        return True
