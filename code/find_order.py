from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        课程表 II
        现在你总共有 n 门课需要选，记为 0 到 n-1。
        在选修某些课程之前需要一些先修课程。
        例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
        可能会有多个正确的顺序，你只要返回一种就可以了。
        如果不可能完成所有课程，返回一个空数组。

        :param numCourses:
        :param prerequisites:
        :return:
        """
        in_degree_list = [0] * numCourses
        adjacent_table = [set() for _ in range(numCourses)]
        for end, start in prerequisites:
            in_degree_list[end] += 1
            adjacent_table[start].add(end)

        next_list = []
        for i in range(len(in_degree_list)):
            if in_degree_list[i] == 0:
                next_list.append(i)

        result_list = []
        while next_list:
            current_node = next_list.pop(0)
            result_list.append(current_node)
            for next_node in adjacent_table[current_node]:
                in_degree_list[next_node] -= 1
                if in_degree_list[next_node] == 0:
                    next_list.append(next_node)
        if len(result_list) < numCourses:
            return []
        return result_list
