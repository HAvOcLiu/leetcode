from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        segments = [''] * 4 
        def dfs(seg_id, seg_start):
            # 从s[set_start]的位置开始
            # 检索IP地址的第seg_id段
            # 其中，seg_id ∈ [0, 3]
            if seg_id == 4:
                # 已经集齐了4段ip片段
                if seg_start == n:
                    # 字符串s恰好遍历完了
                    # 得到了一个合格的候选，加入答案
                    candidate = ".".join(segments)
                    ans.append(candidate)
                return None
            
            if seg_start == n:
                # 进入这里说明还没有得到4段ip，但是字符串已经遍历完了
                # 没有合格的候选，回溯
                return None
            
            # 下面的情况就是没有集齐4段ip且字符串s还没有遍历完
            if s[seg_start] == '0':
                # 0开头的话，这个片段就只能是0了
                segments[seg_id] = "0"
                dfs(seg_id+1, seg_start+1);
                return None
            
            # 非0开头的情况
            for seg_end in range(seg_start, n):
                addr = int(s[seg_start:seg_end+1])
                if 0 <= addr <= 255:
                    segments[seg_id] = str(addr)
                    dfs(seg_id+1, seg_end+1)
                else:
                    break
        dfs(0, 0)
        return ans


solution = Solution()
test_input = "25525511135"
result = solution.restoreIpAddresses(test_input)
print(result)
