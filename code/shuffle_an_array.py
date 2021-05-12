import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self._nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self._nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self._nums[:]
        random.shuffle(nums)
        return nums
