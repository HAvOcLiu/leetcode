from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 合并K个排序链表
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        num_lists = len(lists)
        if num_lists < 1:
            return None

        interval = 1
        while interval < num_lists:
            for i in range(0, num_lists - interval, interval * 2):  # range(start, stop, step)
                lists[i] = self._merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]

    def _merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode(0)
        p = head
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list1
                list1 = p.next.next
            p = p.next
        if list1:
            p.next = list1
        else:
            p.next = list2
        return head.next
