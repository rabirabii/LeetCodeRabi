class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        cur = 0
        hashmap = {0: -1}

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            prefix = (cur - remain + p) % p
            if prefix in hashmap:
                res = min(res, i - hashmap[prefix])
            hashmap[cur] = i

        return res if res == len(nums) else -1
