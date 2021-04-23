from typing import List


class Solution:
    # 三数之和
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums_len = len(nums)
        if nums_len < 3:
            return result

        nums.sort()
        for i in range(nums_len - 2):  # 走到倒数第三个就行了，后面元素不够，不管了
            if nums[i] > 0:
                return result  # 因为已经升序排列了，后面怎么加都是正数，加不出0了
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 数字重复会得到相同的解，跳过
            j = i + 1
            k = nums_len - 1
            while j < k:
                sum_now = nums[i] + nums[j] + nums[k]
                if sum_now == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1  # j向后，躲过重复元素
                    j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1  # k向前，躲过重复元素
                    k -= 1
                elif sum_now < 0:
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1  # 结果小于0，说明不够大，j向后走，换一个更大的数
                    j += 1  # while循环结束，nums[j]！=nums[j+1]，那j+1这个位置才是我们要的数字
                else:
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1  # 结果大于0，说明不够小，k向前走，换一个小点儿的数
                    k -= 1  # 同理， 最后把k再向前挪一个位置

        return result
