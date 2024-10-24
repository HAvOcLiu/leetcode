from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        滑动窗口最大值
        给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
        你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
        返回滑动窗口中的最大值。

        :param nums:
        :param k:
        :return:
        """

        len_nums = len(nums)  # 输入数组的长度
        my_queue = []  # 双端队列，存储数组下标
        for i in range(k):
            # 用第一个窗口初始化队列
            while my_queue and nums[i] >= nums[my_queue[-1]]:
                # 在窗口范围里，新看到的值大于等于队尾元素
                # 队尾元素就不要了，因为新的值大，原先那个不会成为最大值了
                my_queue.pop()
            my_queue.append(i)  # 把这个大的值加入到队尾
        # 这时候队列的第一个元素就是第一个窗口的最大值
        result_list = [nums[my_queue[0]]]  # 保存第一个最大值
        for i in range(k, len_nums):
            # 初始化完成之后，从k位置开始遍历整个数组
            while my_queue and nums[i] >= nums[my_queue[-1]]:
                # 原理是一样的，如果队列不空，而且新看到的值大于等于队尾元素
                # 队尾元素就不要了
                # 每次新看到一个值，这个值就是窗口向右移动一个位置造成的变化
                # 如果这个值是大的，那我们之前保留的所有的小于这个值的都不可能成为最大值了
                my_queue.pop()
            # 新见到的值一定在当前窗口范围里
            # 所以即便把队列清空了，也不会丢掉最大值
            my_queue.append(i)  # 把这个新的大值加入队尾
            # 最坏情况下，输入的数组是一个降序排序好的数组
            # 所有的数组元素依次加入队尾
            # 随着窗口滑动，数组元素依次从队首出队
            # 队列的最大长度就是窗口的大小
            # 不能保证队列里存储的位置一定在当前窗口范围里
            # 但是保证队列里的元素是递减的，这样就依次记录了第一大的、第二大的、……、第N大的位置
            while my_queue[0] <= i - k:
                # 队首元素已经不在当前窗口范围里了
                # 把它移出队列
                my_queue.pop(0)
            # 新的队首元素就是当前窗口的最大值
            result_list.append(nums[my_queue[0]])  # 保存最大值
        return result_list
