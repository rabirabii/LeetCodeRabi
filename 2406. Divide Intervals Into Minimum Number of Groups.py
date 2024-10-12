class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start, end = [], []

        for left, right in intervals:
            start.append(left)
            end.append(right)

        start.sort()
        end.sort()

        i, j = 0, 0
        ans = 0

        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            res = max(res, i - 1)

        return ans


# Second Approach
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start, end = [], []

        for left, right in intervals:
            start.append(left)
            end.append(right)

        start.sort()
        end.sort()

        i, j = 0, 0
        ans = 0
        groups = 0

        while i < len(intervals):
            if start[i] <= end[j]:
                groups += 1
                i += 1
            else:
                groups -= 1
                j += 1
            ans = max(ans, groups)

        return ans
