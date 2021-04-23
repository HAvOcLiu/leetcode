class MinStack:
    """
    最小栈
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    """

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._my_stack = []
        self._min_value = -1

    def push(self, val: int) -> None:
        """
        将元素 x 推入栈中
        :param val:
        :return:
        """
        if not self._my_stack:
            # 如果目前栈空
            self._my_stack.append(0)
            self._min_value = val
        else:
            # 目前栈不空
            diff = val - self._min_value  # 入栈值与最小值的差
            self._my_stack.append(diff)  # 把这个差入栈
            if diff < 0:
                # diff<0说明入栈的值要比当前的最小值还要小
                # 把当前的最小值更新为要入栈的值
                self._min_value = val

    def pop(self) -> None:
        """
        删除栈顶的元素
        :return:
        """
        diff = self._my_stack.pop()  # 取栈顶元素，实际上是一个入栈的值与最小值的差值
        if diff < 0:
            # 如果差值小于0，说明这次入栈的值是最小值
            # 删掉这个元素之后，最小值就要变大
            # 变大的方法是给最小值加上这个差值
            # 减负如加正
            self._min_value -= diff

    def top(self) -> int:
        """
        获取栈顶元素
        :return:
        """
        top_val = self._my_stack[-1]  # 拿到栈顶元素，这个元素实际上是真正的栈顶值与最小值的差值
        if top_val < 0:
            # 这个差值小于0，说明当前最小值就是真正的栈顶值
            return self._min_value
        else:
            # 否则就给当前最小值加上这个差值，还原出实际的栈顶值
            return self._min_value + top_val

    def getMin(self) -> int:
        """
        检索栈中的最小元素
        :return:
        """
        return self._min_value
