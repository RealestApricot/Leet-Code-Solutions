class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Solution = 0
        for num in nums:
            Solution ^= num
        return Solution
