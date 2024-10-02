class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [rank[num] for num in arr]
