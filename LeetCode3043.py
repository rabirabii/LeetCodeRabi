#  Neetcode
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n // 10

        res = 0
        for n in arr2:
            while n and n not in prefix_set:
                n = n // 10

            if n:
                res = max(res, len(str(n)))
        return res


# My Answer
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        def get_prefixes(num):
            prefixes = set()
            while num:
                prefixes.add(num)
                num //= 10
            return prefixes

        prefix_set = set()
        for num in arr1:
            prefix_set.update(get_prefixes(num))

        max_length = 0
        for num in arr2:
            curr_prefixes = get_prefixes(num)
            common_prefixes = curr_prefixes.intersection(prefix_set)
            if common_prefixes:
                max_length = max(max_length, len(str(max(common_prefixes))))

        return max_length
