from typing import List


class Solution:
    def _partition(self, a: List[int], left: int, right: int) -> int:
        pivot = a[left]
        while left < right:
            while left < right and a[right] >= pivot:
                right -= 1
            a[left] = a[right]
            while left < right and a[left] <= pivot:
                left += 1
            a[right] = a[left]
        a[left] = pivot
        return left

    def _quick_sort(self, a: List[int], left: int, right: int):
        if left < right:
            k = self._partition(a, left, right)
            self._quick_sort(a, left, k - 1)
            self._quick_sort(a, k + 1, right)

    def _quick_sort_non_recursive(self, a: List[int], left: int, right: int):
        stack = []
        if left < right:
            stack.append(right)
            stack.append(left)
            while stack:
                current_left = stack.pop()
                current_right = stack.pop()
                k = self._partition(a, current_left, current_right)
                if current_left < k - 1:
                    stack.append(k - 1)
                    stack.append(current_left)
                if current_right > k + 1:
                    stack.append(current_right)
                    stack.append(k + 1)

    def qsort(self, a: List[int]):
        self._quick_sort_non_recursive(a, 0, len(a) - 1)
        print(a)


if __name__ == '__main__':
    solution = Solution()
    solution.qsort([49, 38, 13, 27, 76, 97, 65, 49])
