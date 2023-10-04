class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestLength = 0
        left = 0
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 1:
            return 1
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] - nums[i-1] != 1:
                if len(nums[left:i]) > longestLength:
                    longestLength = len(nums[left:i])
                left = i
            if i == len(nums)-1:
                if len(nums[left:len(nums)]) > longestLength:
                    longestLength = len(nums[left:len(nums)])
        return longestLength
