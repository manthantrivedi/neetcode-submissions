class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n=len(nums)

        ans = ans+nums
        ans = ans+nums

        return ans