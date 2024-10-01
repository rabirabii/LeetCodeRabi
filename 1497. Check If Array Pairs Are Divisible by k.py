class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            num %= k
            if num < 0:
                num += k
            freq[num] += 1

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        if k % 2 == 0 and freq[k // 2] % 2 == 1:
            return False
        return True
