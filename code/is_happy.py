class Solution:
    def isHappy(self, n: int) -> bool:
        """
        快乐数
        编写一个算法来判断一个数 n 是不是快乐数。
        「快乐数」定义为：
            对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
            然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
            如果 可以变为1，那么这个数就是快乐数。

        :param n:
        :return:
        """
        n_permitted = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100}
        if n in n_permitted:
            return True  # 这些是已知的快乐数，如果输入在这里面，直接返回True

        n_passed = {2, 4, 37, 42, 16, 145, 20, 89, 58}
        if n in n_passed:
            return False  # 这些是已知的，无限循环的，如果输入在这里面，肯单不是，返回False
        n_passed.add(n)  # 输入不在里面，加入返回False的集合，循环到自己就返回False

        while True:
            n = sum([int(n_char) ** 2 for n_char in str(n)])
            if n in n_permitted:
                return True
            if n in n_passed:
                return False
            n_passed.add(n)
